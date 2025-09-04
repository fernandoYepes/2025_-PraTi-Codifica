// src/App.jsx
import { Routes, Route, Link } from 'react-router-dom';
import HomePage from './pages/HomePage';
import DetailsPage from './pages/DetailsPage';
import FavoritesPage from './pages/FavoritesPage';
import './App.css';

function App() {
  return (
    // Vamos remover o <div className="container"> daqui
    // e deixar o controle do layout para o CSS.
    <>
      <nav className="navbar">
        <Link to="/">Busca</Link>
        <Link to="/favorites">Favoritos</Link>
      </nav>
      
      <main className="main-content">
        <Routes>
          <Route path="/" element={<HomePage />} />
          <Route path="/movie/:id" element={<DetailsPage />} />
          <Route path="/favorites" element={<FavoritesPage />} />
        </Routes>
      </main>
    </>
  );
}

export default App;