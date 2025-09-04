// src/pages/HomePage.jsx

import { useState, useEffect } from 'react'; // 1. Importe o useEffect
import axios from 'axios';
import MovieCard from '../components/MovieCard';

const HomePage = () => {
  const [query, setQuery] = useState('');
  const [movies, setMovies] = useState([]);
  const [currentPage, setCurrentPage] = useState(1);
  const [totalPages, setTotalPages] = useState(0);
  
  const API_KEY = import.meta.env.VITE_TMDB_API_KEY;

  // 2. NOVO: useEffect para buscar filmes populares ao carregar a página
  useEffect(() => {
    const fetchPopularMovies = async () => {
      try {
        const response = await axios.get('https://api.themoviedb.org/3/movie/popular', {
          params: {
            api_key: API_KEY,
            language: 'pt-BR',
            page: 1,
          }
        });
        setMovies(response.data.results);
        setTotalPages(response.data.total_pages);
      } catch (error) {
        console.error("Erro ao buscar filmes populares:", error);
      }
    };

    fetchPopularMovies();
  }, []); // O array vazio [] significa que este efeito só roda UMA VEZ, quando o componente é montado.

  const handleSearch = async (e, pageNumber = 1) => {
    if (e) {
      e.preventDefault();
    }
    
    if (!query) return;

    // A lógica de busca continua exatamente a mesma...
    try {
      const response = await axios.get('https://api.themoviedb.org/3/search/movie', {
        params: {
          api_key: API_KEY,
          query: query,
          language: 'pt-BR',
          page: pageNumber,
        }
      });
      setMovies(response.data.results);
      setCurrentPage(response.data.page);
      setTotalPages(response.data.total_pages);
    } catch (error) {
      console.error("Erro ao buscar filmes:", error);
    }
  };

  const handlePageChange = (newPage) => {
    handleSearch(null, newPage);
  };

  return (
    <>
      <h1>Meu App de Filmes</h1>
      
      <form onSubmit={handleSearch}>
        <input 
          type="text" 
          placeholder="Digite o nome de um filme"
          value={query}
          onChange={(e) => setQuery(e.target.value)}
        />
        <button type="submit">Buscar</button>
      </form>

      <div className="movie-list">
        {movies.map(movie => (
          <MovieCard key={movie.id} movie={movie} />
        ))}
      </div>

      {totalPages > 1 && (
        <div className="pagination">
          <button 
            onClick={() => handlePageChange(currentPage - 1)} 
            disabled={currentPage === 1}
          >
            Anterior
          </button>
          <span>Página {currentPage} de {totalPages}</span>
          <button 
            onClick={() => handlePageChange(currentPage + 1)} 
            disabled={currentPage === totalPages}
          >
            Próxima
          </button>
        </div>
      )}
    </>
  );
}

export default HomePage;