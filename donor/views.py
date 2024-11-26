# donor/views.py

# donor/views.py
from rest_framework import viewsets
from .serializers import DonorSerializer
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse, reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from .models import Donor
from .forms import DonorForm


class DonorListView(ListView):
    model = Donor
    template_name = 'donors/donor_list.html'
    context_object_name = 'donors'


class DonorCreateView(CreateView):
    model = Donor
    form_class = DonorForm
    template_name = 'donors/donor_form.html'  

    def form_valid(self, form):
    
        return super().form_valid(form)

    def get_success_url(self):
       
        return reverse('donor:donor_list')  
    

class DonorUpdateView(UpdateView):
    model = Donor
    template_name = 'donors/donor_form.html'
    fields = ['name', 'email', 'phone', 'address']
    success_url = reverse_lazy('donor:donor_list')

    def form_valid(self, form):
        return super().form_valid(form)


class DonorDeleteView(DeleteView):
    model = Donor
    template_name = 'donors/donor_confirm_delete.html'
    success_url = reverse_lazy('donor:donor_list')


class DonorViewSet(viewsets.ModelViewSet):
    queryset = Donor.objects.all()
    serializer_class = DonorSerializer
    def get_queryset(self):
        event_id = self.request.query_params.get('event_id')
        if event_id:
            return self.queryset.filter(event_id=event_id)
        return self.queryset
