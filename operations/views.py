from rest_framework import viewsets
from .models import TripAssignment
from .serializers import TripAssignmentSerializer
from users.permissions import IsDriver

class TripAssignmentViewSet(viewsets.ModelViewSet):
    """
    ViewSet for managing Trip Assignments.
    Admins/Managers see all. Drivers only see their own assignments.
    """
    serializer_class = TripAssignmentSerializer
    permission_classes = [IsDriver]

    def get_queryset(self):
        user = self.request.user
        if user.role in ['ADMIN', 'MANAGER']:
            return TripAssignment.objects.all()
        # Drivers only see trips where they are the assigned driver
        return TripAssignment.objects.filter(driver=user)
