# donor/models.py
from django.db import models
from event.models import Event  # Import Event model from the 'event' app

class Donor(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField()
    amount_donated = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    event = models.ForeignKey(Event, on_delete=models.CASCADE)  # ForeignKey to Event
    address = models.CharField(max_length=255)
    country = models.CharField(max_length=255)
    phone = models.CharField(max_length=20)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
