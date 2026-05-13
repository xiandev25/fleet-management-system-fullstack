from rest_framework import serializers
from .models import Vehicle, MaintenanceLog

class VehicleSerializer(serializers.ModelSerializer):
    status_display = serializers.CharField(source='get_status_display', read_only=True)

    class Meta:
        model = Vehicle
        fields = [
            'id', 'brand', 'model', 'license_plate', 'immatriculation_number',
            'manufacture_year', 'current_mileage', 'status', 'status_display',
            'created_at', 'updated_at'
        ]

class MaintenanceLogSerializer(serializers.ModelSerializer):
    vehicle_plate = serializers.CharField(source='vehicle.license_plate', read_only=True)
    job_type_display = serializers.CharField(source='get_job_type_display', read_only=True)

    class Meta:
        model = MaintenanceLog
        fields = [
            'id', 'vehicle', 'vehicle_plate', 'action_taken', 'job_type', 
            'job_type_display', 'mechanic', 'completion_date', 
            'next_service_mileage', 'cost', 'notes'
        ]
