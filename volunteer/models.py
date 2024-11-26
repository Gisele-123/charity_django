# volunteer/models.py

from django.db import models
from event.models import Event  # Import Event model from the 'event' app

class Volunteer(models.Model):
    name = models.CharField(max_length=100)  # Volunteer name
    email = models.EmailField(max_length=255)  # Email address
    phone = models.CharField(max_length=15)  # Phone number
    skills = models.TextField()  # Skills description
    created_at = models.DateTimeField(auto_now_add=True)  # Timestamp for creation
    event = models.ForeignKey(Event, related_name='volunteers', on_delete=models.CASCADE)

    def __str__(self):
        return self.name
