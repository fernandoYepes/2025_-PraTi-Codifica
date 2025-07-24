document.addEventListener('DOMContentLoaded', () => {

    // --- LÓGICA DO CARROSSEL DE HABILIDADES ---
    const wrapper = document.querySelector('.habilidades-wrapper');
    const prevBtn = document.getElementById('btn-prev-skill');
    const nextBtn = document.getElementById('btn-next-skill');
    const slides = document.querySelectorAll('.habilidades-slide');
    const totalSlides = slides.length;
    let currentIndex = 0;

    function updateCarousel() {
        // Move o wrapper para mostrar o slide correto
        wrapper.style.transform = `translateX(-${currentIndex * 100}%)`;

        // Esconde ou mostra os botões de navegação
        if (currentIndex === 0) {
            prevBtn.classList.add('hidden');
        } else {
            prevBtn.classList.remove('hidden');
        }

        if (currentIndex === totalSlides - 1) {
            nextBtn.classList.add('hidden');
        } else {
            nextBtn.classList.remove('hidden');
        }
    }

    // Evento para o botão "Próximo"
    nextBtn.addEventListener('click', () => {
        if (currentIndex < totalSlides - 1) {
            currentIndex++;
            updateCarousel();
        }
    });

    // Evento para o botão "Anterior"
    prevBtn.addEventListener('click', () => {
        if (currentIndex > 0) {
            currentIndex--;
            updateCarousel();
        }
    });

    // Inicia o carrossel no estado correto
    updateCarousel();

});