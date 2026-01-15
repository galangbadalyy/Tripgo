document.addEventListener('DOMContentLoaded', function() {
    
    // --- KONFIGURASI TAB ---
    const tabBtns = document.querySelectorAll('.tab-btn');
    const tabContents = document.querySelectorAll('.tab-content');

    // Definisi Style untuk setiap mode (agar warnanya sesuai design)
    const styles = {
        'pesawat': {
            activeBtn: ['text-blue-600', 'border-blue-600'],
            activeIcon: ['bg-blue-50'],
            inactiveBtn: ['text-gray-400', 'border-transparent', 'hover:text-blue-600', 'hover:border-blue-600'],
            inactiveIcon: ['bg-gray-50', 'group-hover:bg-blue-50']
        },
        'kereta': {
            activeBtn: ['text-orange-600', 'border-orange-600'],
            activeIcon: ['bg-orange-50'],
            inactiveBtn: ['text-gray-400', 'border-transparent', 'hover:text-orange-600', 'hover:border-orange-600'],
            inactiveIcon: ['bg-gray-50', 'group-hover:bg-orange-50']
        },
        'bus': {
            activeBtn: ['text-green-600', 'border-green-600'],
            activeIcon: ['bg-green-50'],
            inactiveBtn: ['text-gray-400', 'border-transparent', 'hover:text-green-600', 'hover:border-green-600'],
            inactiveIcon: ['bg-gray-50', 'group-hover:bg-green-50']
        }
    };

    function switchTab(targetTab) {
        // 1. Sembunyikan semua konten form
        tabContents.forEach(content => {
            if (content.id === targetTab + '-form') {
                content.classList.remove('hidden');
                content.classList.add('block', 'animate-fade-in-up');
            } else {
                content.classList.add('hidden');
                content.classList.remove('block', 'animate-fade-in-up');
            }
        });

        // 2. Update Style Tombol
        tabBtns.forEach(btn => {
            const mode = btn.getAttribute('data-tab');
            const iconBox = btn.querySelector('div'); // div pembungkus icon
            const currentStyle = styles[mode];

            // Reset class dasar
            btn.className = 'tab-btn group flex items-center space-x-3 border-b-2 pb-2 px-1 whitespace-nowrap transition cursor-pointer';
            iconBox.className = 'p-2.5 rounded-lg transition';

            if (mode === targetTab) {
                // Style Aktif
                btn.classList.add(...currentStyle.activeBtn);
                iconBox.classList.add(...currentStyle.activeIcon);
            } else {
                // Style Tidak Aktif
                btn.classList.add(...currentStyle.inactiveBtn);
                iconBox.classList.add(...currentStyle.inactiveIcon);
            }
        });
    }

    // Event Listener untuk klik Tab
    tabBtns.forEach(btn => {
        btn.addEventListener('click', () => {
            switchTab(btn.getAttribute('data-tab'));
        });
    });

    // --- FITUR SWAP LOKASI (Tukar Asal & Tujuan) ---
    function setupSwap(btnId, inputAsalName, inputTujuanName) {
        const btn = document.getElementById(btnId);
        if(!btn) return;

        btn.addEventListener('click', function() {
            // Ambil elemen input berdasarkan 'name'
            const inputAsal = document.querySelector(`input[name="${inputAsalName}"]`);
            const inputTujuan = document.querySelector(`input[name="${inputTujuanName}"]`);
            
            if (inputAsal && inputTujuan) {
                // Tukar nilai
                const temp = inputAsal.value;
                inputAsal.value = inputTujuan.value;
                inputTujuan.value = temp;

                // Efek animasi putar ikon
                const icon = this.querySelector('i');
                icon.style.transition = 'transform 0.3s';
                icon.style.transform = 'rotate(180deg)';
                setTimeout(() => {
                    icon.style.transform = 'rotate(0deg)'; // Reset rotasi jika ingin diputar lagi nanti
                }, 300);
            }
        });
    }

    // Inisialisasi tombol swap untuk masing-masing mode
    setupSwap('swap-pesawat', 'asal', 'tujuan');
    setupSwap('swap-kereta', 'asal_kereta', 'tujuan_kereta');
    setupSwap('swap-bus', 'asal_bus', 'tujuan_bus');
});