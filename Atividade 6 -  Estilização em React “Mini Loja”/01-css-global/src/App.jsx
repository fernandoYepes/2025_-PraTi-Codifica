// src/App.jsx
import React from 'react';
import { products } from './data/products';
import ProductCard from './components/ProductCard/ProductCard';
import { useTheme } from './hooks/useTheme';
import SkeletonCard from './components/SkeletonCard/SkeletonCard';

function App() {
  const { theme, toggleTheme } = useTheme();
  const [isLoading, setIsLoading] = React.useState(true);

  React.useEffect(() => {
    const timer = setTimeout(() => setIsLoading(false), 2000);
    return () => clearTimeout(timer);
  }, []);

  return (
    <>
      <nav style={{ padding: '1rem', borderBottom: '1px solid #ccc', display: 'flex', justifyContent: 'space-between', alignItems: 'center' }}>
        <h1>Minha Loja</h1>
        <button onClick={toggleTheme}>
          Mudar para tema {theme === 'light' ? 'Escuro' : 'Claro'}
        </button>
      </nav>

      <main>
        <div className="product-grid">
          {/* 2. Altere a lógica do loading aqui */}
          {isLoading
            ? (
                // Se estiver carregando, mostre 6 Skeletons
                Array.from({ length: 6 }).map((_, index) => <SkeletonCard key={index} />)
              )
            : (
                // Se não estiver carregando, mostre os produtos
                products.map((product) => (
                  <ProductCard key={product.id} product={product} />
                ))
              )
          }
        </div>
      </main>
    </>
  );
}

export default App;