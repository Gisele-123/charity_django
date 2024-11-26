# donor/urls.py

from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import DonorViewSet
from .views import DonorListView, DonorCreateView, DonorUpdateView, DonorDeleteView

app_name = "donor" 

router = DefaultRouter()
router.register(r'donors', DonorViewSet)

urlpatterns = [
    # path('', include(router.urls)),
    path('', DonorListView.as_view(), name='donor_list'),
    path('create/', DonorCreateView.as_view(), name='donor_create'),
    path('<int:pk>/edit/', DonorUpdateView.as_view(), name='donor_edit'),
    path('<int:pk>/delete/', DonorDeleteView.as_view(), name='donor_delete'),
]
