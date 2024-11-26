from rest_framework import viewsets
from .models import Volunteer
from .forms import VolunteerForm
from .serializers import VolunteerSerializer
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from rest_framework.permissions import IsAuthenticated, AllowAny 

# This should be a ListView for regular Django page rendering
class VolunteerListView(ListView):
    model = Volunteer
    template_name = 'volunteer/volunteer_list.html'
    context_object_name = 'volunteers'  # This defines the name of the context variable passed to the template

# CreateView for adding a new volunteer
class VolunteerCreateView(CreateView):
    model = Volunteer
    form_class = VolunteerForm
    template_name = 'volunteer/volunteer_form.html'
    success_url = reverse_lazy('volunteer_list') 

    def form_valid(self, form):
        return super().form_valid(form)

# UpdateView for editing an existing volunteer
class VolunteerUpdateView(UpdateView):
    model = Volunteer
    template_name = 'volunteer/volunteer_form.html'
    fields = ['name', 'email', 'phone', 'skills']

    def form_valid(self, form):
        return super().form_valid(form)

# DeleteView for confirming and deleting a volunteer
class VolunteerDeleteView(DeleteView):
    model = Volunteer
    template_name = 'volunteer/volunteer_confirm_delete.html'
    success_url = reverse_lazy('volunteer_list')


# ViewSet for API endpoints (This is for API routes, not Django views)
class VolunteerViewSet(viewsets.ModelViewSet):
    queryset = Volunteer.objects.all()
    serializer_class = VolunteerSerializer
    permission_classes = [AllowAny]  # Make sure the API is protected by authentication
