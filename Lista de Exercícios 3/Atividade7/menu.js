// Pega elementos do HTML 
const hamburgerButton = document.getElementById('hamburger-button');
const mainNav = document.getElementById('main-nav');

// Adiciona um "ouvinte de evento"
hamburgerButton.addEventListener('click', () => {
    // cada clique, ele alterna
    // chave" que ativa e desativa as animações
    document.body.classList.toggle('nav-open');
});