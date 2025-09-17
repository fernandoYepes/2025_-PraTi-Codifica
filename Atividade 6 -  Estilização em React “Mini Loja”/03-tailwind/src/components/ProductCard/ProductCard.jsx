// src/components/ProductCard/ProductCard.jsx
import React from 'react';
import styles from './ProductCard.module.css'; // 1. Importa os estilos como um objeto
import Button from '../Button/Button'; // O caminho para o botão também mudou

const ProductCard = ({ product }) => {
  return (
    // 2. Usa as classes do objeto 'styles'
    <article className={styles.card} tabIndex="0">
      <div className={styles.imageWrapper}>
        <img
          src={product.image}
          alt={product.title}
          className={styles.image}
          loading="lazy"
        />
      </div>
      <div className={styles.content}>
        <h3 className={styles.title}>{product.title}</h3>
        <div className={styles.info}>
          <span className={styles.price}>R$ {product.price.toFixed(2)}</span>
          <span className={styles.rating}>★ {product.rating}</span>
        </div>
        <div className={styles.buttonWrapper}>
          <Button variant="solid">Adicionar</Button>
        </div>
      </div>
    </article>
  );
};

export default ProductCard;