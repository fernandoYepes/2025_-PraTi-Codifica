// src/components/MovieCard.jsx
import { Link } from 'react-router-dom'; // 1. Importe o Link

const MovieCard = ({ movie }) => {
  const imageUrl = movie.poster_path
    ? `https://image.tmdb.org/t/p/w500${movie.poster_path}`
    : 'https://via.placeholder.com/500x750.png?text=No+Image';

  const releaseYear = movie.release_date ? movie.release_date.substring(0, 4) : 'N/A';

  return (
    <div className="movie-card">
      <img src={imageUrl} alt={movie.title} />
      <div className="movie-info">
        <h3>{movie.title}</h3>
        <p>{releaseYear}</p>
        {/* 2. Substitua o <button> por este <Link> */}
        <Link to={`/movie/${movie.id}`} className="details-button">
          Ver Detalhes
        </Link>
      </div>
    </div>
  );
};

export default MovieCard;