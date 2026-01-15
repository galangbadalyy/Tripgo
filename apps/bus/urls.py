from django.urls import path
from . import views

app_name = 'bus'

urlpatterns = [
    # Halaman Utama Bus
    path('', views.home, name='home'),
    
    # Search Action
    path('search/', views.bus_search, name='bus_search'),
    
    # Detail Page
    path('detail/<int:bus_id>/', views.bus_detail, name='bus_detail'),
    
    # Halaman Form Booking (PERBAIKAN NAMA)
    # Ubah name='booking_page' menjadi 'bus_booking' agar sesuai dengan template detail
    path('booking/<int:bus_id>/', views.booking_page, name='bus_booking'),
    
    # Halaman Sukses
    path('booking/confirm/', views.booking_confirm, name='booking_confirm'),
]