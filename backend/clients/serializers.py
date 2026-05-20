from rest_framework import serializers
from .models import Family, Student

class StudentSerializer(serializers.ModelSerializer):
    assigned_line_name = serializers.CharField(source='assigned_line.name', read_only=True)
    assigned_shuttle_name = serializers.CharField(source='assigned_shuttle.name', read_only=True)

    class Meta:
        model = Student
        fields = [
            'id', 'family', 'first_name', 'last_name', 'student_registration_number',
            'date_of_birth', 'assigned_line', 'assigned_line_name', 
            'assigned_shuttle', 'assigned_shuttle_name', 'created_at'
        ]

class FamilySerializer(serializers.ModelSerializer):
    # Nesting students so a guardian gets their whole family info in one go
    students = StudentSerializer(many=True, read_only=True)
    primary_guardian_name = serializers.CharField(source='primary_guardian.get_full_name', read_only=True)

    class Meta:
        model = Family
        fields = [
            'id', 'primary_guardian', 'primary_guardian_name', 'secondary_guardian',
            'family_registration_number', 'billing_address', 'students', 'created_at'
        ]
