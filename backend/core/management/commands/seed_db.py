from django.core.management.base import BaseCommand
from django.contrib.auth import get_user_model

User = get_user_model()

class Command(BaseCommand):
    help = 'Seeds the database with initial data for testing/development'

    def handle(self, *args, **kwargs):
        self.stdout.write('Seeding data...')
        
        # Seed Superuser
        if not User.objects.filter(username='admin').exists():
            User.objects.create_superuser('admin', 'admin@example.com', 'adminpass123')
            self.stdout.write(self.style.SUCCESS('Successfully created superuser "admin" with password "adminpass123"'))
        else:
            self.stdout.write(self.style.WARNING('Superuser "admin" already exists.'))
            
        # You can add more seed logic here for Vehicles, Routes, etc.
        # e.g., from fleet.models import Vehicle
        
        self.stdout.write(self.style.SUCCESS('Database seeding completed successfully.'))
