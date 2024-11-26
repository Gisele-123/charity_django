# event/models.py
from django.db import models

class Event(models.Model):
    title = models.CharField(max_length=200)  # New field for the event title
    name = models.CharField(max_length=100)
    date = models.DateField()
    location = models.CharField(max_length=255)  # New field for location
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
