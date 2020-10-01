from django.urls import path
from . import views

urlpatterns = [
    path('', views.hotel_list),
    path('<int:id>/', views.hotel_detail),
]