from hotel.models import Domain
from django.urls import path
from . import views

urlpatterns = [
    path('hotel/<int:id>', views.hotel_detail),
    path('domain', views.domain_list)
]