from django.db import models
from django.conf import settings
from django.core.exceptions import ValidationError

class TripAssignment(models.Model):
    class TimeSlot(models.TextChoices):
        MORNING = "MORNING", "Morning"
        AFTERNOON = "AFTERNOON", "Afternoon"

    class Status(models.TextChoices):
        SCHEDULED = "SCHEDULED", "Scheduled"
        IN_PROGRESS = "IN_PROGRESS", "In Progress"
        COMPLETED = "COMPLETED", "Completed"
        CANCELLED = "CANCELLED", "Cancelled"

    vehicle = models.ForeignKey(
        'fleet.Vehicle', 
        on_delete=models.CASCADE, 
        related_name='trips'
    )
    driver = models.ForeignKey(
        settings.AUTH_USER_MODEL, 
        on_delete=models.CASCADE, 
        related_name='trips'
    )
    # A trip can be either for a standard Bus Line or a Shuttle
    bus_line = models.ForeignKey(
        'routes.BusLine', 
        on_delete=models.SET_NULL, 
        null=True, 
        blank=True, 
        related_name='trips'
    )
    shuttle = models.ForeignKey(
        'routes.Shuttle', 
        on_delete=models.SET_NULL, 
        null=True, 
        blank=True, 
        related_name='trips'
    )
    
    date = models.DateField()
    time_slot = models.CharField(max_length=20, choices=TimeSlot.choices)
    status = models.CharField(
        max_length=20, 
        choices=Status.choices, 
        default=Status.SCHEDULED
    )
    
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def clean(self):
        # 1. Mutually exclusive route assignment
        if self.bus_line and self.shuttle:
            raise ValidationError("A trip cannot be assigned to both a Bus Line and a Shuttle.")
        if not self.bus_line and not self.shuttle:
            raise ValidationError("A trip must have either a Bus Line or a Shuttle assigned.")

        # 2. Vehicle Conflict Detection
        vehicle_conflicts = TripAssignment.objects.filter(
            vehicle=self.vehicle,
            date=self.date,
            time_slot=self.time_slot
        ).exclude(pk=self.pk)
        if vehicle_conflicts.exists():
            raise ValidationError(f"Vehicle {self.vehicle} is already assigned to another trip on this date and time slot.")

        # 3. Driver Conflict Detection
        driver_conflicts = TripAssignment.objects.filter(
            driver=self.driver,
            date=self.date,
            time_slot=self.time_slot
        ).exclude(pk=self.pk)
        if driver_conflicts.exists():
            raise ValidationError(f"Driver {self.driver} is already assigned to another trip on this date and time slot.")

        # 4. Check Vehicle availability status
        if self.vehicle.status in ['IN_MAINTENANCE', 'IN_REPAIR', 'RETIRED']:
            raise ValidationError(f"Vehicle {self.vehicle} cannot be assigned because its status is {self.vehicle.get_status_display()}.")

    def save(self, *args, **kwargs):
        self.full_clean()
        super().save(*args, **kwargs)

    def __str__(self):
        route = self.bus_line.name if self.bus_line else self.shuttle.name
        return f"Trip: {route} | {self.date} ({self.time_slot})"
