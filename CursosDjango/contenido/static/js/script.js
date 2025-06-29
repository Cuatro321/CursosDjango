document.addEventListener('DOMContentLoaded', function() {
    const faders = document.querySelectorAll('.fade-in');
    const appearOptions = { threshold: 0.2 };
    const appearOnScroll = new IntersectionObserver((entries, observer) => {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                entry.target.classList.add('visible');
                observer.unobserve(entry.target);
            }
        });
    }, appearOptions);
    faders.forEach(fader => appearOnScroll.observe(fader));

    // Botón volver arriba
    const btnBack = document.getElementById('btn-back-to-top');
    window.addEventListener('scroll', () => {
        if (window.scrollY > 300) {
            btnBack.style.display = 'flex';
        } else {
            btnBack.style.display = 'none';
        }
    });
    btnBack.addEventListener('click', () => {
        window.scrollTo({ top: 0, behavior: 'smooth' });
    });

    // Smooth scroll para enlaces internos
    document.querySelectorAll('a[href^="#"]').forEach(anchor => {
        anchor.addEventListener('click', function (e) {
            e.preventDefault();
            const targetID = this.getAttribute('href');
            const targetEl = document.querySelector(targetID);
            if (targetEl) {
                targetEl.scrollIntoView({ behavior: 'smooth', block: 'start' });
            }
        });
    });

    // Validación simple de formulario contacto
    const form = document.querySelector('#contact-form');
    if (form) {
        form.addEventListener('submit', function(e) {
            let valid = true;
            const nombre = form.querySelector('input[name="nombre"]');
            const correo = form.querySelector('input[name="correo"]');
            if (!nombre.value.trim()) {
                valid = false;
                nombre.classList.add('is-invalid');
            } else {
                nombre.classList.remove('is-invalid');
            }
            if (!correo.value.trim() || !correo.value.includes('@')) {
                valid = false;
                correo.classList.add('is-invalid');
            } else {
                correo.classList.remove('is-invalid');
            }
            if (!valid) {
                e.preventDefault();
            }
        });
    }
});
