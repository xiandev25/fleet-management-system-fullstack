from django.contrib import admin
from .models import BusLine, BusStop, Shuttle

class BusStopInline(admin.TabularInline):
    model = BusStop
    extra = 1

@admin.register(BusLine)
class BusLineAdmin(admin.ModelAdmin):
    list_display = ('name', 'description')
    inlines = [BusStopInline]

@admin.register(BusStop)
class BusStopAdmin(admin.ModelAdmin):
    list_display = ('name', 'line', 'sequence_number', 'scheduled_time')
    list_filter = ('line',)
    ordering = ('line', 'sequence_number')

@admin.register(Shuttle)
class ShuttleAdmin(admin.ModelAdmin):
    list_display = ('name', 'pickup_point', 'scheduled_time')
