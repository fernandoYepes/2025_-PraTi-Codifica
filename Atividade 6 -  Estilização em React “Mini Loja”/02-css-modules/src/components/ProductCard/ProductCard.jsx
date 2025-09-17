import React from 'react';
import styles from './ProductCard.module.css';
import Button from '../Button/Button'; // O caminho da importação mudou!

const ProductCard = ({ product }) => {
  return (
    <article className={styles.card} tabIndex="0">
      <div className={styles.imageWrapper}>
        <img src={product.image} className={styles.image} alt={product.title} loading="lazy" />
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