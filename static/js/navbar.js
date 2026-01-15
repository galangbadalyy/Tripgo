    // Navbar Scroll Logic
    const navbar = document.getElementById('navbar');
    const navLinks = document.querySelectorAll('.nav-link');
    const navLogoText = document.getElementById('nav-logo-text');
    const navContainer = document.getElementById('navbar-container');
    const navIconBtns = document.querySelectorAll('.nav-icon-btn');
    
    // Auth Elements (might be null if not logged in)
    const navDivider = document.getElementById('nav-divider');
    const navWelcome = document.getElementById('nav-welcome');
    const navUsername = document.getElementById('nav-username');
    const btnDashboard = document.getElementById('btn-dashboard');
    const btnRegister = document.getElementById('btn-register');

    window.addEventListener('scroll', () => {
        if (window.scrollY > 20) {
            // === SCROLLED STATE (White Background) ===
            navbar.classList.remove('bg-transparent', 'py-2');
            navbar.classList.add('bg-white/90', 'backdrop-blur-md', 'shadow-md', 'py-0');
            
            // Shrink container height slightly
            navContainer.classList.remove('md:h-20');
            navContainer.classList.add('md:h-16');

            // Text Colors -> Dark
            navLogoText.classList.remove('text-white');
            navLogoText.classList.add('text-blue-900');

            navLinks.forEach(link => {
                link.classList.remove('text-white/90', 'text-white/80', 'hover:bg-white/10');
                link.classList.add('text-gray-600', 'hover:bg-blue-50', 'hover:text-blue-600');
            });
            
            navIconBtns.forEach(btn => {
                btn.classList.remove('text-white', 'text-white/80');
                btn.classList.add('text-gray-600');
            });

            // Auth Elements Update
            if(navDivider) {
                navDivider.classList.remove('border-white/20');
                navDivider.classList.add('border-gray-200');
            }
            if(navWelcome) {
                navWelcome.classList.remove('text-blue-100');
                navWelcome.classList.add('text-gray-400');
            }
            if(navUsername) {
                navUsername.classList.remove('text-white');
                navUsername.classList.add('text-gray-900');
            }
            if(btnDashboard) {
                btnDashboard.classList.remove('bg-white/20', 'text-white', 'border-white/20');
                btnDashboard.classList.add('bg-blue-600', 'text-white', 'border-transparent', 'hover:bg-blue-700');
            }
            if(btnRegister) {
                btnRegister.classList.remove('bg-white', 'text-blue-900');
                btnRegister.classList.add('bg-blue-600', 'text-white');
            }

        } else {
            // === TOP STATE (Transparent) ===
            navbar.classList.add('bg-transparent', 'py-2');
            navbar.classList.remove('bg-white/90', 'backdrop-blur-md', 'shadow-md', 'py-0');
            
            navContainer.classList.add('md:h-20');
            navContainer.classList.remove('md:h-16');

            // Text Colors -> White
            navLogoText.classList.add('text-white');
            navLogoText.classList.remove('text-blue-900');

            navLinks.forEach(link => {
                link.classList.add('text-white/90', 'hover:bg-white/10');
                link.classList.remove('text-gray-600', 'hover:bg-blue-50', 'hover:text-blue-600');
                // Khusus nav link yang bukan 'Beranda' (index 0 biasanya active)
                if(!link.classList.contains('font-bold')) { 
                     link.classList.add('text-white/80');
                }
            });

            navIconBtns.forEach(btn => {
                btn.classList.add('text-white');
                btn.classList.remove('text-gray-600');
            });

            // Auth Elements Reset
            if(navDivider) {
                navDivider.classList.add('border-white/20');
                navDivider.classList.remove('border-gray-200');
            }
            if(navWelcome) {
                navWelcome.classList.add('text-blue-100');
                navWelcome.classList.remove('text-gray-400');
            }
            if(navUsername) {
                navUsername.classList.add('text-white');
                navUsername.classList.remove('text-gray-900');
            }
            if(btnDashboard) {
                btnDashboard.classList.add('bg-white/20', 'text-white', 'border-white/20');
                btnDashboard.classList.remove('bg-blue-600', 'border-transparent', 'hover:bg-blue-700');
            }
            if(btnRegister) {
                btnRegister.classList.add('bg-white', 'text-blue-900');
                btnRegister.classList.remove('bg-blue-600', 'text-white');
            }
        }
    });

    // Mobile Menu Toggle (Simple Logic)
    const btnMobile = document.getElementById('mobile-menu-btn');
    const menuMobile = document.getElementById('navbar-menu');

    btnMobile.addEventListener('click', () => {
        menuMobile.classList.toggle('hidden');
    });