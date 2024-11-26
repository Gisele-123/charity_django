# volunteer/urls.py

from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import VolunteerViewSet
from .views import VolunteerListView, VolunteerCreateView, VolunteerUpdateView, VolunteerDeleteView

router = DefaultRouter()
router.register(r'volunteers', VolunteerViewSet)  # This is for API endpoints

urlpatterns = [
   
    path('api/', include(router.urls)),  

    # Regular views for the website
    path('', VolunteerListView.as_view(), name='volunteer_list'),
    path('create/', VolunteerCreateView.as_view(), name='volunteer_create'),
    path('<int:pk>/edit/', VolunteerUpdateView.as_view(), name='volunteer_edit'),
    path('<int:pk>/delete/', VolunteerDeleteView.as_view(), name='volunteer_delete'),
]
