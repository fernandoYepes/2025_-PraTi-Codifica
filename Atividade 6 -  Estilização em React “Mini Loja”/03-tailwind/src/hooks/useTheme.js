// src/hooks/useTheme.js
import { useState, useEffect } from 'react';

export const useTheme = () => {
  // Tenta pegar o tema do localStorage ou usa a preferência do sistema
  const [theme, setTheme] = useState(() => {
    const savedTheme = localStorage.getItem('theme');
    const prefersDark = window.matchMedia && window.matchMedia('(prefers-color-scheme: dark)').matches;
    return savedTheme || (prefersDark ? 'dark' : 'light');
  });

  // Efeito que roda toda vez que o tema muda
  useEffect(() => {
    // Adiciona o atributo `data-theme` no elemento <html>
    document.documentElement.setAttribute('data-theme', theme);
    // Salva a preferência no localStorage
    localStorage.setItem('theme', theme);
  }, [theme]);

  // Função para inverter o tema
  const toggleTheme = () => {
    setTheme((prevTheme) => (prevTheme === 'light' ? 'dark' : 'light'));
  };

  return { theme, toggleTheme };
};