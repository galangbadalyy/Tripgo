from django.shortcuts import render
from django.http import HttpResponse
from apps.pesawat.dummy_data import FLIGHTS_DUMMY
from apps.kereta.dummy_data import TRAINS_DUMMY
from apps.bus.dummy_data import BUS_DUMMY


def home(request):
    """Halaman home/index dengan 3 section transportasi"""
    # Ambil 3 tiket termurah dari masing-masing transportasi
    pesawat_tickets = sorted(FLIGHTS_DUMMY, key=lambda x: x['price'])[:3]
    kereta_tickets = sorted(TRAINS_DUMMY, key=lambda x: x['price'])[:3]
    bus_tickets = sorted(BUS_DUMMY, key=lambda x: x['price'])[:3]
    
    context = {
        'pesawat_tickets': pesawat_tickets,
        'kereta_tickets': kereta_tickets,
        'bus_tickets': bus_tickets,
    }
    return render(request, 'core/home.html', context)


def about(request):
    """Halaman tentang kami"""
    return render(request, 'core/about.html')


def contact(request):
    """Halaman kontak"""
    return render(request, 'core/contact.html')


def gallery(request):
    """Halaman galeri/destinasi"""
    # Ambil semua tiket dari ketiga transportasi
    all_tickets = []
    
    # Normalisasi pesawat
    for flight in FLIGHTS_DUMMY:
        all_tickets.append({
            'id': flight['id'],
            'type': 'pesawat',
            'from_city': flight['from_city'],
            'to_city': flight['to_city'],
            'image': flight.get('airline_logo', ''),
            'price': flight['price'],
            'badge': flight.get('badge_text'),
        })
    
    # Normalisasi kereta
    for train in TRAINS_DUMMY:
        all_tickets.append({
            'id': train['id'],
            'type': 'kereta',
            'from_city': train['from_city'],
            'to_city': train['to_city'],
            'image': train.get('operator_logo', ''),
            'price': train['price'],
            'badge': train.get('badge_text'),
        })
    
    # Normalisasi bus
    for bus in BUS_DUMMY:
        all_tickets.append({
            'id': bus['id'],
            'type': 'bus',
            'from_city': bus['from_city'],
            'to_city': bus['to_city'],
            'image': bus.get('operator_logo', ''),
            'price': bus['price'],
            'badge': bus.get('badge_text'),
        })
    
    context = {
        'tickets': all_tickets,
    }
    
    return render(request, 'core/gallery.html', context)