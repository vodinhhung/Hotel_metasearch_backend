from django.urls import path
from django.conf.urls import url 
from . import views

urlpatterns = [
    url(r'^hotel/province$', views.province_list),
    url(r'^hotel$', views.hotel_list),
    path('hotel/<int:id>/', views.hotel_detail),
    path('hotel/login', views.login_user),
]