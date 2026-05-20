from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import BusLineViewSet, BusStopViewSet, ShuttleViewSet

router = DefaultRouter()
router.register(r'lines', BusLineViewSet)
router.register(r'stops', BusStopViewSet)
router.register(r'shuttles', ShuttleViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
