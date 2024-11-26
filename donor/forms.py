# donor/forms.py
from django import forms
from .models import Donor, Event

class DonorForm(forms.ModelForm):
    class Meta:
        model = Donor
        fields = ['name', 'email', 'amount_donated', 'event', 'address', 'country', 'phone']

    # Define the event field to be a dropdown of available events
    event = forms.ModelChoiceField(queryset=Event.objects.all(), empty_label="Select Event")
