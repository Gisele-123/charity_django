from django.contrib import admin
from django.urls import path, include
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from . import views
from django.contrib.auth import views as auth_views
from rest_framework.routers import DefaultRouter
from donor.views import DonorViewSet
from volunteer.views import VolunteerViewSet
from event.views import EventViewSet, PublicEventViewSet

# Initialize the DefaultRouter
router = DefaultRouter()
router.register(r'donors', DonorViewSet)
router.register(r'volunteers', VolunteerViewSet)
router.register(r'events', EventViewSet, basename='event')  # Provide a unique basename for EventViewSet
router.register(r'public-events', PublicEventViewSet, basename='public-event')  # Provide a unique basename for PublicEventViewSet

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),

    path('donors/', include('donor.urls', namespace="donor")), 
    path('volunteers/', include('volunteer.urls')),
    path('events/', include('event.urls')),

    path('register/', views.register, name='register'),
    path('login/', views.login, name='login'),
    path('logout/', auth_views.LogoutView.as_view(next_page='/login/'), name='logout'),

    path('dashboard/', views.dashboard_view, name='dashboard'),

    # API Endpoints for events, donors, volunteers
    path('api/', include(router.urls)),  # This will include routes for donors, volunteers, events

    # JWT Authentication
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/core/', include('core.urls')),
]
