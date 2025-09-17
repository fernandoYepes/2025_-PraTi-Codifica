// src/components/SkeletonCard/SkeletonCard.jsx
import React from 'react';
import styles from './SkeletonCard.module.css';

const SkeletonCard = () => {
  return (
    <div className={styles.card}>
      <div className={`${styles.skeleton} ${styles.image}`}></div>
      <div className={`${styles.skeleton} ${styles.title}`}></div>
      <div className={`${styles.skeleton} ${styles.info}`}></div>
      <div className={`${styles.skeleton} ${styles.button}`}></div>
    </div>
  );
};

export default SkeletonCard;