from django.db.models import Q
from rest_framework import viewsets
from .models import Invoice
from .serializers import InvoiceSerializer
from users.permissions import IsFamilyGuardian

class InvoiceViewSet(viewsets.ModelViewSet):
    """
    ViewSet for Invoices.
    Admins/Managers see all. Guardians only see their family's invoices.
    """
    serializer_class = InvoiceSerializer
    permission_classes = [IsFamilyGuardian]

    def get_queryset(self):
        user = self.request.user
        if user.role in ['ADMIN', 'MANAGER']:
            return Invoice.objects.all()
        # Guardians only see invoices linked to their family
        return Invoice.objects.filter(
            Q(family__primary_guardian=user) | 
            Q(family__secondary_guardian=user)
        )
