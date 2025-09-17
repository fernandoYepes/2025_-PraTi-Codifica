// src/components/Button/Button.jsx
import React from 'react';
import styles from './Button.module.css'; // 1. Importa os estilos locais

const Button = ({ children, variant = 'solid', ...props }) => {
  // 2. Constrói a classe dinamicamente a partir do objeto styles
  // Acessa a classe 'btn' e a classe da variante, por ex: styles['solid']
  const className = `${styles.btn} ${styles[variant]}`;

  return (
    <button className={className} {...props}>
      {children}
    </button>
  );
};

export default Button;