from django.db.models import Q
from rest_framework import viewsets
from .models import Family, Student
from .serializers import FamilySerializer, StudentSerializer
from users.permissions import IsFamilyGuardian

class FamilyViewSet(viewsets.ModelViewSet):
    """
    ViewSet for Families.
    Admins/Managers see all. Guardians only see their own family.
    """
    serializer_class = FamilySerializer
    permission_classes = [IsFamilyGuardian]

    def get_queryset(self):
        user = self.request.user
        # Admins and Managers see everything
        if user.role in ['ADMIN', 'MANAGER']:
            return Family.objects.all()
        # Guardians only see families where they are primary or secondary
        return Family.objects.filter(Q(primary_guardian=user) | Q(secondary_guardian=user))

class StudentViewSet(viewsets.ModelViewSet):
    """
    ViewSet for Students.
    Admins/Managers see all. Guardians only see their children.
    """
    serializer_class = StudentSerializer
    permission_classes = [IsFamilyGuardian]

    def get_queryset(self):
        user = self.request.user
        if user.role in ['ADMIN', 'MANAGER']:
            return Student.objects.all()
        # Guardians only see students linked to their family
        return Student.objects.filter(Q(family__primary_guardian=user) | Q(family__secondary_guardian=user))
