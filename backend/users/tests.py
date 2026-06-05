from django.test import TestCase
from django.contrib.auth import get_user_model

User = get_user_model()

class UserTestCase(TestCase):
    def setUp(self):
        User.objects.create_user(username='testuser', password='testpassword123', email='test@example.com')

    def test_user_creation(self):
        """Test that a user can be successfully created"""
        user = User.objects.get(username='testuser')
        self.assertEqual(user.email, 'test@example.com')
        self.assertTrue(user.check_password('testpassword123'))

    def test_superuser_creation(self):
        """Test that a superuser can be created"""
        admin = User.objects.create_superuser(username='admin_test', password='adminpassword123', email='admin@example.com')
        self.assertTrue(admin.is_superuser)
        self.assertTrue(admin.is_staff)
