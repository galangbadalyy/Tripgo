document.addEventListener('DOMContentLoaded', function () {

    // ======================================================
    // BAGIAN 1: LOGIKA GANTI TAB (WARNA-WARNI)
    // ======================================================
    const tabBtns = document.querySelectorAll('.tab-btn');
    const tabContents = document.querySelectorAll('.tab-content');

    tabBtns.forEach(btn => {
        btn.addEventListener('click', (e) => {
            e.preventDefault();
            const tabName = btn.getAttribute('data-tab');

            // 1. RESET SEMUA TOMBOL KE TAMPILAN MATI (ABU-ABU)
            tabBtns.forEach(b => {
                // Hapus semua kemungkinan warna aktif
                b.classList.remove(
                    'text-blue-600', 'border-blue-600', 
                    'text-orange-600', 'border-orange-600', 
                    'text-green-600', 'border-green-600', 
                    'border-b-2', 'active'
                );
                // Tambahkan warna abu-abu
                b.classList.add('text-gray-400');

                // Reset background icon jadi abu-abu
                const iconDiv = b.querySelector('div');
                if (iconDiv) {
                    iconDiv.className = iconDiv.className
                        .replace('bg-blue-50', 'bg-gray-50')
                        .replace('bg-orange-50', 'bg-gray-50')
                        .replace('bg-green-50', 'bg-gray-50');
                }
            });

            // 2. SEMBUNYIKAN SEMUA FORM
            tabContents.forEach(content => {
                content.classList.add('hidden');
                content.classList.remove('block');
            });

            // 3. AKTIFKAN TOMBOL YANG DIKLIK (BERI WARNA SESUAI JENIS)
            btn.classList.remove('text-gray-400');
            btn.classList.add('border-b-2', 'active');
            
            const activeIconDiv = btn.querySelector('div');

            if (tabName === 'pesawat') {
                // Set warna Biru
                btn.classList.add('text-blue-600', 'border-blue-600');
                if(activeIconDiv) activeIconDiv.classList.replace('bg-gray-50', 'bg-blue-50');
            } 
            else if (tabName === 'kereta') {
                // Set warna Orange
                btn.classList.add('text-orange-600', 'border-orange-600');
                if(activeIconDiv) activeIconDiv.classList.replace('bg-gray-50', 'bg-orange-50');
            } 
            else if (tabName === 'bus') {
                // Set warna Hijau
                btn.classList.add('text-green-600', 'border-green-600');
                if(activeIconDiv) activeIconDiv.classList.replace('bg-gray-50', 'bg-green-50');
            }

            // 4. MUNCULKAN FORM YANG SESUAI
            const targetForm = document.getElementById(`${tabName}-form`);
            if (targetForm) {
                targetForm.classList.remove('hidden');
                targetForm.classList.add('block');
            }
        });
    });


    // ======================================================
    // BAGIAN 2: LOGIKA SWAP LOCATION (TUKAR ASAL/TUJUAN)
    // ======================================================
    function setupSwap(btnId, inputAsalName, inputTujuanName) {
        const btn = document.getElementById(btnId);
        const inputAsal = document.querySelector(`input[name="${inputAsalName}"]`);
        const inputTujuan = document.querySelector(`input[name="${inputTujuanName}"]`);

        if (btn && inputAsal && inputTujuan) {
            btn.addEventListener('click', function (e) {
                e.preventDefault();
                
                // Tukar text value
                const temp = inputAsal.value;
                inputAsal.value = inputTujuan.value;
                inputTujuan.value = temp;

                // Animasi putar icon
                const icon = this.querySelector('i');
                if(icon) {
                    icon.style.transition = 'transform 0.4s ease';
                    icon.style.transform = 'rotate(180deg)';
                    setTimeout(() => { icon.style.transform = 'rotate(0deg)'; }, 400);
                }
            });
        }
    }

    // Jalankan fungsi swap untuk ketiga tab
    setupSwap('swap-pesawat', 'asal', 'tujuan');
    setupSwap('swap-kereta', 'asal_kereta', 'tujuan_kereta');
    setupSwap('swap-bus', 'asal_bus', 'tujuan_bus');

});