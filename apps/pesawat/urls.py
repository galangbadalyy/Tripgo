from django.urls import path
from . import views

app_name = 'pesawat'

urlpatterns = [
    path('', views.home, name='home'),
    path('search/', views.flight_search, name='flight_search'),
    path('detail/<int:flight_id>/', views.flight_detail, name='flight_detail'),
    path('booking/<int:flight_id>/', views.flight_booking, name='flight_booking'),
    path('booking/confirm/', views.booking_confirm, name='booking_confirm'),

]