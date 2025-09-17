// src/components/ProductCard.jsx
import React from 'react';

const ProductCard = ({ product }) => {
  return (
    <article
      className="flex flex-col overflow-hidden rounded-lg bg-surface dark:bg-dark-surface border border-border dark:border-dark-border shadow-md transition-all duration-200 hover:-translate-y-1 hover:shadow-lg focus-within:ring-2 focus-within:ring-primary dark:focus-within:ring-dark-primary"
      tabIndex="0"
    >
      <div className="aspect-square bg-background dark:bg-dark-background">
        <img
          src={product.image}
          alt={product.title}
          className="h-full w-full object-cover"
          loading="lazy"
        />
      </div>
      <div className="flex flex-1 flex-col p-4">
        <h3 className="text-base font-semibold text-text-primary dark:text-dark-text-primary h-[3.2em] leading-tight line-clamp-2">
          {product.title}
        </h3>
        <div className="mt-2 mb-4 flex items-center justify-between">
          <span className="text-xl font-bold text-text-primary dark:text-dark-text-primary">
            R$ {product.price.toFixed(2)}
          </span>
          <span className="text-sm text-text-secondary dark:text-dark-text-secondary">
            ★ {product.rating}
          </span>
        </div>
        <button className="mt-auto w-full rounded-lg bg-primary dark:bg-dark-primary px-4 py-2 font-semibold text-white transition-opacity hover:opacity-90">
          Adicionar
        </button>
      </div>
    </article>
  );
};

export default ProductCard;