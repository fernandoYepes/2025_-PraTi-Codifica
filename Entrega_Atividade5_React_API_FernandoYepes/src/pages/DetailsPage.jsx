// src/pages/DetailsPage.jsx

import { useEffect, useState } from 'react';
import { useParams } from 'react-router-dom';
import axios from 'axios';
import useFavorites from '../hooks/useFavorites'; // Importa o nosso novo hook

const DetailsPage = () => {
  const { id } = useParams();
  const [movie, setMovie] = useState(null);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(null);

  // Chamamos o hook para ter acesso às funções de favoritos
  const { addFavorite, removeFavorite, isFavorite } = useFavorites();

  const API_KEY = import.meta.env.VITE_TMDB_API_KEY;

  // Esta é a parte que estava faltando, a busca dos dados do filme
  useEffect(() => {
    const fetchMovieDetails = async () => {
      setLoading(true);
      setError(null);
      try {
        const response = await axios.get(`https://api.themoviedb.org/3/movie/${id}`, {
          params: {
            api_key: API_KEY,
            language: 'pt-BR'
          }
        });
        setMovie(response.data);
      } catch (err) {
        setError('Erro ao carregar os detalhes do filme.');
        console.error(err);
      } finally {
        setLoading(false);
      }
    };

    fetchMovieDetails();
  }, [id]);

  // As verificações de loading, erro e se o filme existe
  if (loading) {
    return <p style={{ textAlign: 'center', fontSize: '1.5rem' }}>Carregando...</p>;
  }
  if (error) {
    return <p style={{ color: 'red', textAlign: 'center' }}>{error}</p>;
  }
  if (!movie) {
    return null;
  }

  // A definição da URL da imagem
  const imageUrl = movie.poster_path
    ? `https://image.tmdb.org/t/p/w500${movie.poster_path}`
    : 'https://via.placeholder.com/500x750.png?text=No+Image';

  // A nova função para lidar com o clique no botão de favorito
  const handleFavoriteClick = () => {
    if (isFavorite(movie.id)) {
      removeFavorite(movie.id);
    } else {
      const movieData = {
        id: movie.id,
        title: movie.title,
        poster_path: movie.poster_path,
        release_date: movie.release_date
      };
      addFavorite(movieData);
    }
  };

  return (
    <div className="details-page">
      <img src={imageUrl} alt={movie.title} className="details-poster" />
      <div className="details-info">
        <h1>{movie.title}</h1>
        <p className="tagline">{movie.tagline}</p>
        <p className="overview"><strong>Sinopse:</strong> {movie.overview}</p>
        <p><strong>Avaliação:</strong> {movie.vote_average ? movie.vote_average.toFixed(1) : 'N/A'} / 10</p>
        <p><strong>Data de Lançamento:</strong> {new Date(movie.release_date).toLocaleDateString('pt-BR')}</p>
        <p><strong>Gêneros:</strong> {movie.genres.map(genre => genre.name).join(', ')}</p>

        {/* O novo botão de favoritos */}
        <button onClick={handleFavoriteClick} className="favorite-button">
          {isFavorite(movie.id) ? 'Remover dos Favoritos' : 'Adicionar aos Favoritos'}
        </button>
      </div>
    </div>
  );
};

export default DetailsPage;