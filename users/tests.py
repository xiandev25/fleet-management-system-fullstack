from django.test import TestCase
from django.contrib.auth import get_user_model
from rest_framework.test import APIRequestFactory
from users.permissions import IsAdmin, IsManager, IsDriver, IsGuardian

User = get_user_model()

class UserRoleTestCase(TestCase):
    def setUp(self):
        self.factory = APIRequestFactory()

    def test_create_user_default_role(self):
        """Verify that newly created users default to the GUARDIAN role."""
        user = User.objects.create_user(
            username='testguardian',
            password='securepassword123'
        )
        self.assertEqual(user.role, User.Role.GUARDIAN)
        self.assertFalse(user.is_staff)
        self.assertFalse(user.is_superuser)

    def test_create_superuser_role_enforcement(self):
        """Verify superuser creation enforces staff, superuser, and ADMIN role flags."""
        admin = User.objects.create_superuser(
            username='testadmin',
            email='admin@fleetflow.local',
            password='securepassword123'
        )
        self.assertEqual(admin.role, User.Role.ADMIN)
        self.assertTrue(admin.is_staff)
        self.assertTrue(admin.is_superuser)

    def test_rbac_permission_classes(self):
        """Verify custom RBAC permission rules act as secure barriers per user role."""
        admin_user = User.objects.create_user(username='admin_u', role=User.Role.ADMIN)
        manager_user = User.objects.create_user(username='manager_u', role=User.Role.MANAGER)
        driver_user = User.objects.create_user(username='driver_u', role=User.Role.DRIVER)
        guardian_user = User.objects.create_user(username='guardian_u', role=User.Role.GUARDIAN)

        # Mock requests
        request_admin = self.factory.get('/')
        request_admin.user = admin_user

        request_manager = self.factory.get('/')
        request_manager.user = manager_user

        request_driver = self.factory.get('/')
        request_driver.user = driver_user

        request_guardian = self.factory.get('/')
        request_guardian.user = guardian_user

        # 1. IsAdmin check - only Admin allowed
        perm_admin = IsAdmin()
        self.assertTrue(perm_admin.has_permission(request_admin, None))
        self.assertFalse(perm_admin.has_permission(request_manager, None))
        self.assertFalse(perm_admin.has_permission(request_driver, None))
        self.assertFalse(perm_admin.has_permission(request_guardian, None))

        # 2. IsManager check - Admin & Manager allowed, others blocked
        perm_manager = IsManager()
        self.assertTrue(perm_manager.has_permission(request_admin, None))
        self.assertTrue(perm_manager.has_permission(request_manager, None))
        self.assertFalse(perm_manager.has_permission(request_driver, None))
        self.assertFalse(perm_manager.has_permission(request_guardian, None))

        # 3. IsDriver check - Admin, Manager & Driver allowed, Guardians blocked
        perm_driver = IsDriver()
        self.assertTrue(perm_driver.has_permission(request_admin, None))
        self.assertTrue(perm_driver.has_permission(request_manager, None))
        self.assertTrue(perm_driver.has_permission(request_driver, None))
        self.assertFalse(perm_driver.has_permission(request_guardian, None))

        # 4. IsGuardian check - Admin, Manager & Guardian allowed, Drivers blocked
        perm_guardian = IsGuardian()
        self.assertTrue(perm_guardian.has_permission(request_admin, None))
        self.assertTrue(perm_guardian.has_permission(request_manager, None))
        self.assertTrue(perm_guardian.has_permission(request_guardian, None))
        self.assertFalse(perm_guardian.has_permission(request_driver, None))
