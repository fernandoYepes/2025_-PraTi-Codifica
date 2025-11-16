🎬 Aplicativo de Busca de Filmes em React
Este projeto foi desenvolvido para praticar e consolidar conceitos fundamentais de React, como componentização, gerenciamento de estado, roteamento e consumo de APIs.

📌 Visão Geral
A aplicação permite que os usuários busquem filmes utilizando a API do The Movie Database (TMDB), visualizem uma lista de resultados, acessem detalhes completos de cada filme e gerenciem uma lista pessoal de favoritos.

🚀 Funcionalidades Implementadas
🔍 Busca e Descoberta
Busca Dinâmica: Campo de texto para buscar filmes por título.
Filmes Populares: Ao abrir a aplicação, a página inicial exibe automaticamente os filmes mais populares do momento.
Paginação: Navegação completa entre as páginas de resultados para explorar toda a lista.

🎥 Detalhes do Filme
Página Dedicada: Ao clicar em um filme, o usuário é levado para uma página com informações detalhadas.
Informações Exibidas: Pôster, título, sinopse, avaliação, data de lançamento e gêneros.

❤️ Lista de Favoritos
Adicionar/Remover: Botão na página de detalhes para favoritar ou remover um filme.
Página de Favoritos: Uma rota /favorites dedicada que exibe todos os filmes salvos.
Persistência de Dados: A lista de favoritos é salva no localStorage do navegador, mantendo os dados mesmo após fechar a página.

⚙️ Experiência do Usuário
Indicadores de Loading: Exibe uma mensagem de "Carregando..." enquanto os dados da API são buscados.
Tratamento de Erros: Mostra mensagens de erro amigáveis na tela caso a busca falhe ou não retorne resultados.
Layout Responsivo e Centralizado: Interface agradável para visualização em desktops.

🛠️ Tecnologias Utilizadas
React (com Vite): Biblioteca principal para a construção da interface.
React Router DOM: Para gerenciar a navegação e as rotas da aplicação.
Axios: Para fazer as chamadas à API do TMDB de forma simples e robusta.
React Hooks: Uso extensivo de useState, useEffect e criação de um Hook customizado (useFavorites).
CSS3: Para a estilização completa da aplicação, utilizando Flexbox e Grid.

⚡ Como Executar o Projeto Localmente
Siga os passos abaixo para configurar e rodar o projeto em sua máquina.
1. Clonar o Repositório
Primeiro, clone o repositório do GitHub:
git clone https://github.com/fernandoYepes/2025_-PraTi-Codifica.git


2. Instalar as Dependências
Navegue até a pasta do projeto. O projeto possui dependências que não estão incluídas no repositório (a pasta node_modules). Execute o comando abaixo para instalá-las. Este passo é obrigatório para o projeto funcionar.
npm install


3. Configurar a Chave da API
Crie um arquivo chamado .env na raiz do projeto e adicione sua chave da API do TMDB.
VITE_TMDB_API_KEY=sua_chave_aqui


4. Iniciar o Servidor de Desenvolvimento
Com tudo instalado, inicie o servidor local:
npm run dev


A aplicação estará disponível em http://localhost:5173 (ou a porta indicada no terminal).
