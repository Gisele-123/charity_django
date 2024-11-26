from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import (
    EventViewSet,
    PublicEventViewSet,
    EventListView,
    EventCreateView,
    EventUpdateView,
    EventDeleteView,
)

app_name = "event"

# Define the router
router = DefaultRouter()
router.register(r'events', EventViewSet, basename='event')  # Authenticated events
router.register(r'public-events', PublicEventViewSet, basename='public_event')  # Public events

urlpatterns = [
    # Include DRF routes
    path('api/', include(router.urls)),  # Use a distinct prefix for API endpoints
    
    # Web app views
    path('', EventListView.as_view(), name='event_list'),  # Main page shows event list
    path('create/', EventCreateView.as_view(), name='event_create'),
    path('<int:pk>/edit/', EventUpdateView.as_view(), name='event_edit'),
    path('<int:pk>/delete/', EventDeleteView.as_view(), name='event_delete'),
]
