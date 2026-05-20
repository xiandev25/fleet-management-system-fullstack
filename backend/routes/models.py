from django.db import models

class BusLine(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)

    def __str__(self):
        return f"Line: {self.name}"

class BusStop(models.Model):
    name = models.CharField(max_length=200)
    line = models.ForeignKey(BusLine, on_delete=models.CASCADE, related_name='stops')
    sequence_number = models.PositiveIntegerField()
    scheduled_time = models.TimeField()
    location_name = models.CharField(max_length=255, blank=True)

    class Meta:
        ordering = ['sequence_number']

    def __str__(self):
        return f"{self.name} ({self.line.name})"

class Shuttle(models.Model):
    name = models.CharField(max_length=100)
    pickup_point = models.CharField(max_length=255)
    scheduled_time = models.TimeField()
    description = models.TextField(blank=True)

    def __str__(self):
        return f"Shuttle: {self.name} - {self.pickup_point}"
