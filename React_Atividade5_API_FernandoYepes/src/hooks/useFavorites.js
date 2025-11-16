// src/hooks/useFavorites.js
import { useState, useEffect } from 'react';

const useFavorites = () => {
  // Inicializamos o estado lendo do localStorage.
  // A função dentro do useState só é executada na primeira renderização.
  const [favorites, setFavorites] = useState(() => {
    try {
      const savedFavorites = localStorage.getItem('myFavoriteMovies');
      return savedFavorites ? JSON.parse(savedFavorites) : [];
    } catch (error) {
      console.error("Failed to parse favorites from localStorage", error);
      return [];
    }
  });

  // Usamos useEffect para observar mudanças no estado 'favorites'.
  // Toda vez que 'favorites' mudar, nós o salvamos no localStorage.
  useEffect(() => {
    localStorage.setItem('myFavoriteMovies', JSON.stringify(favorites));
  }, [favorites]);

  const addFavorite = (movie) => {
    // Adicionamos o filme à lista, garantindo que não haja duplicatas
    if (!favorites.some(fav => fav.id === movie.id)) {
      setFavorites((prevFavorites) => [...prevFavorites, movie]);
    }
  };

  const removeFavorite = (movieId) => {
    setFavorites((prevFavorites) => prevFavorites.filter((movie) => movie.id !== movieId));
  };

  // Função para verificar se um filme já está nos favoritos
  const isFavorite = (movieId) => {
    return favorites.some((movie) => movie.id === movieId);
  };

  // Retornamos o estado e as funções para que os componentes possam usá-los.
  return { favorites, addFavorite, removeFavorite, isFavorite };
};

export default useFavorites;