# event/views.py
from rest_framework import viewsets
from rest_framework.permissions import AllowAny
from .models import Event
from .serializers import EventSerializer
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse_lazy
from rest_framework.permissions import IsAuthenticated, AllowAny  # Import IsAuthenticated


class EventViewSet(viewsets.ModelViewSet):
    queryset = Event.objects.all()
    serializer_class = EventSerializer
    permission_classes = [AllowAny]  # Protect the viewset with authentication

class PublicEventViewSet(viewsets.ModelViewSet):
    queryset = Event.objects.all()
    serializer_class = EventSerializer
    permission_classes = [AllowAny]  # Allow public access to certain event views

class EventListView(ListView):
    model = Event
    template_name = 'events/event_list.html'  # Your template to display the event list
    context_object_name = 'events' 
    
# CreateView for adding a new event
class EventCreateView(CreateView):
    model = Event
    fields = ["title", "name", "date", "location", "description"]  # Include new fields
    template_name = "events/event_form.html"
    success_url = reverse_lazy("event:event_list") 

    def form_valid(self, form):
        return super().form_valid(form)

# UpdateView for editing an existing event
class EventUpdateView(UpdateView):
    model = Event
    template_name = 'events/event_form.html'
    fields = ['title', 'description', 'date', 'location']

    def form_valid(self, form):
        return super().form_valid(form)

# DeleteView for confirming and deleting an event
class EventDeleteView(DeleteView):
    model = Event
    template_name = 'events/event_confirm_delete.html'
    success_url = reverse_lazy('event:event_list')


def create_event(request):
    if request.method == 'POST':
        name = request.POST['name']
        description = request.POST['description']
        date = request.POST['date']

        event = Event(name=name, description=description, date=date)
        event.save()

        return redirect('events')

    return render(request, 'event:event_create.html')