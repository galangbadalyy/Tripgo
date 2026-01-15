from django.shortcuts import render, redirect
from django.http import Http404
from .dummy_data import BUS_DUMMY  # Pastikan file dummy_data.py ada

def home(request):
    """
    View untuk halaman utama Bus (Menampilkan list populer)
    """
    # Ambil data dummy dan sort berdasarkan harga terendah untuk bagian "Populer"
    popular_buses = sorted(BUS_DUMMY, key=lambda x: x['price'])
    
    context = {
        'popular_buses': popular_buses,
    }
    
    # Render ke template home bus
    return render(request, 'bus/home.html', context)


def bus_search(request):
    """
    View untuk menampilkan hasil pencarian bus.
    Logika filter sama persis dengan kereta.
    """
    buses = BUS_DUMMY.copy()
    
    # 1. Ambil parameter dari GET request (Sesuai 'name' di form HTML search_result.html / home.html)
    asal = request.GET.get('asal_bus', '').strip()
    tujuan = request.GET.get('tujuan_bus', '').strip()
    tanggal = request.GET.get('tanggal_bus', '').strip()
    passenger = request.GET.get('penumpang_bus', '1')
    bus_class = request.GET.get('class_bus', 'all').strip()
    
    # 2. Filter Logika
    if asal:
        # Cek apakah input user ada di nama kota atau kode terminal
        buses = [
            b for b in buses 
            if asal.lower() in b['from_city'].lower() 
            or asal.lower() in b['from_code'].lower()
        ]
    
    if tujuan:
        buses = [
            b for b in buses 
            if tujuan.lower() in b['to_city'].lower() 
            or tujuan.lower() in b['to_code'].lower()
        ]
    
    if tanggal:
        buses = [b for b in buses if b['date'] == tanggal]
    
    if bus_class and bus_class != 'all':
        # Filter class (case insensitive)
        buses = [b for b in buses if bus_class.lower() in b['class'].lower()]
    
    # 3. Hitung total harga berdasarkan jumlah penumpang
    try:
        num_passengers = int(passenger)
    except ValueError:
        num_passengers = 1
    
    # Tambahkan properti total_price ke setiap item hasil filter
    for bus in buses:
        bus['total_price'] = bus['price'] * num_passengers
        if bus.get('original_price'): # Pakai .get() jaga-jaga kalau key tidak ada
            bus['total_original_price'] = bus['original_price'] * num_passengers
    
    # Sort hasil pencarian berdasarkan harga termurah
    buses.sort(key=lambda x: x['price'])
    
    context = {
        'buses': buses,  # Variable utama untuk loop di template
        'search_asal': asal,
        'search_tujuan': tujuan,
        'search_tanggal': tanggal,
        'search_penumpang': passenger,
        'search_class': bus_class,
        'num_passengers': num_passengers,
        'total_results': len(buses),
    }
    
    # Render ke template hasil pencarian
    return render(request, 'bus/search_result.html', context)


def bus_detail(request, bus_id):
    """
    View untuk halaman detail/review pesanan bus sebelum booking.
    """
    bus = None
    for b in BUS_DUMMY:
        if b['id'] == bus_id: # Pastikan tipe data ID sama (int vs int)
            bus = b.copy() # Copy agar tidak merubah data asli
            break
    
    if not bus:
        raise Http404("Jadwal bus tidak ditemukan")
    
    # Ambil jumlah penumpang dari query params (default 1)
    try:
        num_passengers = int(request.GET.get('passengers', 1))
    except ValueError:
        num_passengers = 1
    
    # Hitung total untuk ditampilkan di detail
    bus['total_price'] = bus['price'] * num_passengers
    if bus.get('original_price'):
        bus['total_original_price'] = bus['original_price'] * num_passengers
    
    context = {
        'bus': bus,
        'num_passengers': num_passengers,
        'total_price': bus['total_price'], # Kirim explisit biar gampang di template
    }

    return render(request, 'bus/detail_tiket.html', context)


def booking_page(request, bus_id):
    """
    View untuk halaman form pengisian data penumpang (Step 2).
    """
    bus = None
    for b in BUS_DUMMY:
        if b['id'] == bus_id:
            bus = b.copy()
            break
    
    if not bus:
        raise Http404("Jadwal bus tidak ditemukan")
    
    try:
        num_passengers = int(request.GET.get('passengers', 1))
    except ValueError:
        num_passengers = 1
        
    # Hitung total
    bus['total_price'] = bus['price'] * num_passengers
    
    context = {
        'bus': bus,
        'num_passengers': num_passengers,
        'passengers_range': range(1, num_passengers + 1), # Untuk loop form input penumpang
    }
    
    # Kita belum buat template ini, samakan namanya jadi 'bus/booking.html'
    return render(request, 'bus/booking.html', context)


def booking_confirm(request):
    """
    View konfirmasi setelah booking bus disubmit (POST).
    """
    if request.method == 'POST':
        context = {
            'booking_data': request.POST,
        }
        return render(request, 'bus/booking_confirm.html', context)
    
    return redirect('bus:home')