from rest_framework import viewsets
from .models import Vehicle, MaintenanceLog
from .serializers import VehicleSerializer, MaintenanceLogSerializer
from users.permissions import IsMechanic

class VehicleViewSet(viewsets.ModelViewSet):
    """
    ViewSet for viewing and editing vehicles.
    Accessible to Mechanics, Managers, and Admins.
    """
    queryset = Vehicle.objects.all()
    serializer_class = VehicleSerializer
    permission_classes = [IsMechanic]

class MaintenanceLogViewSet(viewsets.ModelViewSet):
    """
    ViewSet for viewing and editing maintenance logs.
    Accessible to Mechanics, Managers, and Admins.
    """
    queryset = MaintenanceLog.objects.all()
    serializer_class = MaintenanceLogSerializer
    permission_classes = [IsMechanic]
