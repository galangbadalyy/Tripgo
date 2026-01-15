from django.shortcuts import render, redirect
from .dummy_data import FLIGHTS_DUMMY
from django.http import Http404


def home(request):
    """
    View untuk halaman home dengan semua sections
    """
    # Ambil semua penerbangan untuk ditampilkan di home (atau bisa dibatasi)
    popular_flights = sorted(FLIGHTS_DUMMY, key=lambda x: x['price'])
    
    context = {
        'popular_flights': popular_flights,
    }
    
    return render(request, 'pesawat/home.html', context)


def flight_search(request):
    """
    View untuk menampilkan hasil pencarian penerbangan
    """
    flights = FLIGHTS_DUMMY.copy()
    
    # Ambil parameter dari GET request
    asal = request.GET.get('asal', '').strip()
    tujuan = request.GET.get('tujuan', '').strip()
    tanggal = request.GET.get('tanggal', '').strip()
    trip_type = request.GET.get('trip_type', 'one-way')
    passenger = request.GET.get('passenger', '1')
    tanggal_kembali = request.GET.get('tanggal_kembali', '').strip()
    flight_class = request.GET.get('class', '').strip()  # Filter class
    
    # Filter hasil pencarian
    if asal:
        # Filter berdasarkan kota asal atau kode bandara
        flights = [
            f for f in flights 
            if asal.lower() in f['from_city'].lower() 
            or asal.lower() in f['from_code'].lower()
        ]
    
    if tujuan:
        # Filter berdasarkan kota tujuan atau kode bandara
        flights = [
            f for f in flights 
            if tujuan.lower() in f['to_city'].lower() 
            or tujuan.lower() in f['to_code'].lower()
        ]
    
    if tanggal:
        # Filter berdasarkan tanggal
        flights = [f for f in flights if f['date'] == tanggal]
    
    if flight_class:
        # Filter berdasarkan class
        flights = [f for f in flights if f['class'].lower() == flight_class.lower()]
    
    # Hitung jumlah passenger
    try:
        num_passengers = int(passenger.split('-')[0]) if '-' in passenger else int(passenger)
    except:
        num_passengers = 1
    
    # Tambahkan informasi total harga per flight
    for flight in flights:
        flight['total_price'] = flight['price'] * num_passengers
        if flight['original_price']:
            flight['total_original_price'] = flight['original_price'] * num_passengers
    
    # Sort berdasarkan harga (termurah dulu)
    flights.sort(key=lambda x: x['price'])
    
    context = {
        'flights': flights,
        'asal': asal,
        'tujuan': tujuan,
        'tanggal': tanggal,
        'tanggal_kembali': tanggal_kembali,
        'trip_type': trip_type,
        'passenger': passenger,
        'num_passengers': num_passengers,
        'flight_class': flight_class,
        'total_results': len(flights),
    }
    
    return render(request, 'pesawat/search_result.html', context)


def flight_detail(request, flight_id):
    """
    View untuk halaman detail penerbangan
    """
    # Cari flight berdasarkan ID
    flight = None
    for f in FLIGHTS_DUMMY:
        if f['id'] == flight_id:
            flight = f.copy()
            break
    
    if not flight:
        raise Http404("Penerbangan tidak ditemukan")
    
    # Ambil passenger dari query string (jika ada)
    num_passengers = int(request.GET.get('passengers', 1))
    
    # Hitung total harga
    flight['total_price'] = flight['price'] * num_passengers
    if flight['original_price']:
        flight['total_original_price'] = flight['original_price'] * num_passengers
    
    context = {
        'flight': flight,
        'num_passengers': num_passengers,
    }
    
    return render(request, 'pesawat/detail-penerbangan.html', context)


def flight_booking(request, flight_id):
    """
    View untuk halaman booking form
    """
    # Cari flight berdasarkan ID
    flight = None
    for f in FLIGHTS_DUMMY:
        if f['id'] == flight_id:
            flight = f.copy()
            break
    
    if not flight:
        raise Http404("Penerbangan tidak ditemukan")
    
    # Ambil passenger dari query string
    num_passengers = int(request.GET.get('passengers', 1))
    
    # Hitung total harga
    flight['total_price'] = flight['price'] * num_passengers
    if flight['original_price']:
        flight['total_original_price'] = flight['original_price'] * num_passengers
    
    context = {
        'flight': flight,
        'num_passengers': num_passengers,
        'passengers_range': range(1, num_passengers + 1),
    }
    
    return render(request, 'pesawat/booking.html', context)


def booking_confirm(request):
    """
    View untuk konfirmasi booking (setelah submit form)
    """
    if request.method == 'POST':
        # Di sini nanti bisa simpan ke database
        # Untuk sekarang, kita tampilkan konfirmasi
        
        context = {
            'booking_data': request.POST,
        }
        
        return render(request, 'pesawat/booking_confirm.html', context)
    
    return redirect('pesawat:home')