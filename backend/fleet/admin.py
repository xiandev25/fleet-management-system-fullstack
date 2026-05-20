from django.contrib import admin
from .models import Vehicle, MaintenanceLog

@admin.register(Vehicle)
class VehicleAdmin(admin.ModelAdmin):
    list_display = ('brand', 'model', 'license_plate', 'status', 'current_mileage')
    list_filter = ('status', 'brand')
    search_fields = ('license_plate', 'immatriculation_number', 'brand', 'model')

@admin.register(MaintenanceLog)
class MaintenanceLogAdmin(admin.ModelAdmin):
    list_display = ('vehicle', 'job_type', 'mechanic', 'completion_date')
    list_filter = ('job_type', 'completion_date')
    search_fields = ('vehicle__license_plate', 'action_taken')
