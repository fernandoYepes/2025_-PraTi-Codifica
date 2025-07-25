// Pega os elementos do HTML que vamos manipular
const hamburgerButton = document.getElementById('hamburger-button');
const mainNav = document.getElementById('main-nav');

// Adiciona um "ouvinte de evento" de clique ao botão
hamburgerButton.addEventListener('click', () => {
    // A cada clique, ele alterna (adiciona/remove) a classe 'nav-open' no body.
    // Esta é a "chave" que ativa e desativa as animações e estilos no CSS.
    document.body.classList.toggle('nav-open');
});