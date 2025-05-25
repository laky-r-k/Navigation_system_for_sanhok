from django.db import models

# Create your models here.
from django.contrib.postgres.fields import ArrayField

class Road(models.Model):
    start_node = models.CharField(max_length=100)
    end_node = models.CharField(max_length=100)
    polyline = ArrayField(
        base_field=models.JSONField(),
        verbose_name="Polyline Coordinates",
        help_text="List of coordinates as JSON: [{lat: ..., lng: ...}, ...]"
    )

    def __str__(self):
        return f"{self.start_node} -> {self.end_node}"