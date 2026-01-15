from django.urls import path
from . import views

app_name = 'kereta'

urlpatterns = [
    path('', views.home, name='home'), # Halaman utama kereta
    path('search/', views.train_search, name='train_search'),
    path('detail/<int:train_id>/', views.train_detail, name='train_detail'),
    path('booking/<int:train_id>/', views.train_booking, name='train_booking'),
    path('booking/confirm/', views.booking_confirm, name='booking_confirm'),
]