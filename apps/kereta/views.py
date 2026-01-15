from django.shortcuts import render, redirect
from django.http import Http404
from .dummy_data import TRAINS_DUMMY  # Pastikan file data.py ada di folder yang sama

def home(request):
    """
    View untuk halaman utama Kereta (Menampilkan list populer)
    """
    # Ambil data dummy dan sort berdasarkan harga terendah untuk bagian "Populer"
    popular_trains = sorted(TRAINS_DUMMY, key=lambda x: x['price'])
    
    context = {
        'popular_trains': popular_trains,
    }
    
    # Render ke template home kereta (yang berisi search bar + list tiket populer)
    return render(request, 'kereta/home.html', context)


def train_search(request):
    """
    View untuk menampilkan hasil pencarian kereta
    """
    trains = TRAINS_DUMMY.copy()
    
    # 1. Ambil parameter dari GET request (Sesuai 'name' di form HTML kereta)
    asal = request.GET.get('asal_kereta', '').strip()
    tujuan = request.GET.get('tujuan_kereta', '').strip()
    tanggal = request.GET.get('tanggal_kereta', '').strip()
    trip_type = request.GET.get('trip_type_ka', 'one-way')
    passenger = request.GET.get('penumpang_kereta', '1')
    train_class = request.GET.get('class_kereta', 'all').strip()
    
    # 2. Filter Logika
    if asal:
        # Cek apakah input user ada di nama kota atau kode stasiun
        trains = [
            t for t in trains 
            if asal.lower() in t['from_city'].lower() 
            or asal.lower() in t['from_code'].lower()
        ]
    
    if tujuan:
        trains = [
            t for t in trains 
            if tujuan.lower() in t['to_city'].lower() 
            or tujuan.lower() in t['to_code'].lower()
        ]
    
    if tanggal:
        trains = [t for t in trains if t['date'] == tanggal]
    
    if train_class and train_class != 'all':
        # Filter class (case insensitive)
        trains = [t for t in trains if train_class.lower() in t['class'].lower()]
    
    # 3. Hitung total harga berdasarkan jumlah penumpang
    try:
        num_passengers = int(passenger)
    except ValueError:
        num_passengers = 1
    
    # Tambahkan properti total_price ke setiap item hasil filter
    for train in trains:
        train['total_price'] = train['price'] * num_passengers
        if train['original_price']:
            train['total_original_price'] = train['original_price'] * num_passengers
    
    # Sort hasil pencarian berdasarkan harga termurah
    trains.sort(key=lambda x: x['price'])
    
    context = {
        'flights': trains, # Kita pakai key 'flights' atau 'trains' (sesuaikan dengan template search_result Anda)
        'trains': trains,  # Saya sediakan key 'trains' agar lebih semantik jika mau ubah template
        'search_asal': asal,
        'search_tujuan': tujuan,
        'search_tanggal': tanggal,
        'search_trip_type': trip_type,
        'search_penumpang': passenger,
        'search_class': train_class,
        'num_passengers': num_passengers,
        'total_results': len(trains),
    }
    
    # Render ke template hasil pencarian
    return render(request, 'kereta/search_result.html', context)


def train_detail(request, train_id):
    """
    View untuk halaman detail tiket kereta
    """
    train = None
    for t in TRAINS_DUMMY:
        if t['id'] == train_id:
            train = t.copy() # Copy agar tidak merubah data asli secara permanen di memory
            break
    
    if not train:
        raise Http404("Jadwal kereta tidak ditemukan")
    
    # Ambil jumlah penumpang dari query params (default 1)
    try:
        num_passengers = int(request.GET.get('passengers', 1))
    except ValueError:
        num_passengers = 1
    
    # Hitung total
    train['total_price'] = train['price'] * num_passengers
    if train['original_price']:
        train['total_original_price'] = train['original_price'] * num_passengers
    
    context = {
        'train': train,
        'num_passengers': num_passengers,
    }

    return render(request, 'kereta/detail_tiket.html', context)


def train_booking(request, train_id):
    """
    View untuk halaman form booking kereta
    """
    train = None
    for t in TRAINS_DUMMY:
        if t['id'] == train_id:
            train = t.copy()
            break
    
    if not train:
        raise Http404("Jadwal kereta tidak ditemukan")
    
    try:
        num_passengers = int(request.GET.get('passengers', 1))
    except ValueError:
        num_passengers = 1
        
    # Hitung total
    train['total_price'] = train['price'] * num_passengers
    
    context = {
        'train': train,
        'num_passengers': num_passengers,
        'passengers_range': range(1, num_passengers + 1), # Untuk loop form input penumpang
    }
    
    return render(request, 'kereta/booking.html', context)


def booking_confirm(request):
    """
    View konfirmasi setelah booking kereta disubmit
    """
    if request.method == 'POST':
        context = {
            'booking_data': request.POST,
        }
        return render(request, 'kereta/booking_confirm.html', context)
    
    return redirect('kereta:home')