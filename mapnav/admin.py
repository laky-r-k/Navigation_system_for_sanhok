from django.contrib import admin
from .models import Road

@admin.register(Road)
class RoadAdmin(admin.ModelAdmin):
    list_display = ('start_node', 'end_node')
    search_fields = ('start_node', 'end_node')
