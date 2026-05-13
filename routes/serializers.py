from rest_framework import serializers
from .models import BusLine, BusStop, Shuttle

class BusStopSerializer(serializers.ModelSerializer):
    class Meta:
        model = BusStop
        fields = ['id', 'line', 'name', 'sequence_number', 'scheduled_time', 'location_lat', 'location_lon']

class BusLineSerializer(serializers.ModelSerializer):
    # Nesting the stops inside the line for a complete view
    stops = BusStopSerializer(many=True, read_only=True)

    class Meta:
        model = BusLine
        fields = ['id', 'name', 'description', 'stops']

class ShuttleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Shuttle
        fields = ['id', 'name', 'pickup_point', 'scheduled_time', 'location_lat', 'location_lon']
