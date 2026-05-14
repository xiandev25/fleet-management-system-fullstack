from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import TripAssignmentViewSet

router = DefaultRouter()
router.register(r'assignments', TripAssignmentViewSet, basename='trip-assignment')

urlpatterns = [
    path('', include(router.urls)),
]
