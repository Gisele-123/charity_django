from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login as auth_login
from django.contrib import messages
from django.shortcuts import render
from donor.models import Donor
from volunteer.models import Volunteer
from event.models import Event
from django.utils.timezone import now
from datetime import timedelta
from collections import defaultdict

from django.contrib.auth.views import LoginView
from django.contrib.auth.decorators import login_required

class CustomLoginView(LoginView):
    template_name = 'login.html' 
    redirect_authenticated_user = True
    next_page = '/dashboard'
from datetime import datetime, timedelta

@login_required
def dashboard_view(request):
    today = datetime.today()
    days = [(today - timedelta(days=i)).date() for i in range(7)]
    donor_counts = []
    volunteer_counts = []
    event_counts = []

    # Ensure created_at exists on these models
    donors = Donor.objects.all().order_by('created_at')
    events = Event.objects.all().order_by('created_at')
    volunteers = Volunteer.objects.all().order_by('created_at')

    # Calculate donors
    for day in days:
        donor_counts.append(Donor.objects.filter(created_at__date=day).count())

    # Calculate volunteers
    for day in days:
        volunteer_counts.append(Volunteer.objects.filter(created_at__date=day).count())

    # Calculate events
    for day in days:
        event_counts.append(Event.objects.filter(created_at__date=day).count())

    context = {
        'days': [day.strftime('%Y-%m-%d') for day in days],
        'donor_data': donor_counts,
        'volunteer_data': volunteer_counts,
        'event_data': event_counts,
    }

    return render(request, 'dashboard.html', {
        'volunteers': volunteers,
        'donors': donors,
        'events': events,
        'context': context
    })

@login_required
def donor_list_view(request):
    donors = Donor.objects.all()
    return render(request, 'donors/donor_list.html', {'donors': donors})

# @login_required
def volunteer_list_view(request):
    volunteers = Volunteer.objects.all()
    return render(request, 'volunteer/volunteer_list.html', {'volunteers': volunteers})


# @login_required
def event_list_view(request):
    events = Event.objects.all()
    return render(request, 'events/event_list.html', {'events': events})

def index(request):
    return render(request, 'index.html')

def register(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        
        user = User.objects.create_user(username=username, email=email, password=password)
        user.save()
        messages.success(request, 'Registration successful! You can now log in.')
        return redirect('login')
    
    return render(request, 'register.html')

def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        
        user = authenticate(request, username=username, password=password)
        if user is not None:
            auth_login(request, user)
            return redirect('dashboard')  
        else:
            messages.error(request, 'Invalid username or password')
    
    return render(request, 'login.html')
