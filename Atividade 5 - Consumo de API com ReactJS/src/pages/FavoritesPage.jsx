// src/pages/FavoritesPage.jsx
import useFavorites from '../hooks/useFavorites';
import MovieCard from '../components/MovieCard';
import { Link } from 'react-router-dom';

const FavoritesPage = () => {
  const { favorites } = useFavorites();

  return (
    <div>
      <h1 style={{ marginBottom: '2rem' }}>Meus Favoritos</h1>
      {favorites.length === 0 ? (
        <p>Você ainda não tem filmes favoritos. Adicione um na página de detalhes!</p>
      ) : (
        <div className="movie-list">
          {favorites.map((movie) => (
            <MovieCard key={movie.id} movie={movie} />
          ))}
        </div>
      )}
    </div>
  );
};

export default FavoritesPage;