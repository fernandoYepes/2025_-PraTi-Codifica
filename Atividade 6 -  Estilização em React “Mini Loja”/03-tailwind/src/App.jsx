// src/App.jsx
import React from 'react';
import { products } from './data/products';
import ProductCard from './components/ProductCard'; // Caminho corrigido
import { useTheme } from './hooks/useTheme';
// import SkeletonCard from './components/SkeletonCard'; // Adicionaremos depois

function App() {
  const { theme, toggleTheme } = useTheme();
  const [isLoading, setIsLoading] = React.useState(true);

  React.useEffect(() => {
    const timer = setTimeout(() => setIsLoading(false), 2000);
    return () => clearTimeout(timer);
  }, []);

  return (
    <div className="min-h-screen bg-background dark:bg-dark-background">
      <nav className="sticky top-0 bg-surface/80 dark:bg-dark-surface/80 backdrop-blur-sm border-b border-border dark:border-dark-border p-4 flex justify-between items-center">
        <h1 className="text-xl font-bold text-text-primary dark:text-dark-text-primary">Minha Loja</h1>
        <button onClick={toggleTheme} className="rounded-lg px-3 py-1 text-text-secondary dark:text-dark-text-secondary hover:bg-black/10 dark:hover:bg-white/10">
          Mudar Tema
        </button>
      </nav>

      <main>
        <div className="grid grid-cols-1 gap-6 p-6 sm:grid-cols-2 lg:grid-cols-3 xl:grid-cols-4">
          {isLoading
            ? <p className="text-text-primary dark:text-dark-text-primary">Carregando...</p>
            : products.map((product) => (
                <ProductCard key={product.id} product={product} />
              ))}
        </div>
      </main>
    </div>
  );
}

export default App;