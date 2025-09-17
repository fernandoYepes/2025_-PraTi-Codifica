// src/components/ProductCard.jsx
import React from 'react';
import Button from './Button'; // <-- Importe o componente

const ProductCard = ({ product }) => {
  return (
    <article className="product-card" tabIndex="0">
      {/* ...resto do card... */}
      <div className="product-card__content">
        {/* ... */}
        {/* Substitua o <button> antigo por este: */}
        <div className="product-card__button">
          <Button variant="solid">Adicionar</Button>
        </div>
      </div>
    </article>
  );
};

export default ProductCard;