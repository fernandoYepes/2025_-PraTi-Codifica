/** @type {import('tailwindcss').Config} */
export default {
  content: [
    "./index.html",
    "./src/**/*.{js,ts,jsx,tsx}",
  ],
  darkMode: 'class',
  theme: {
    extend: {
      colors: {
        'surface': '#ffffff',
        'background': '#f8f9fa',
        'primary': '#0d6efd',
        'text-primary': '#212529',
        'text-secondary': '#6c757d',
        'border': '#dee2e6',
        dark: {
          'surface': '#1e1e1e',
          'background': '#121212',
          'primary': '#3b82f6',
          'text-primary': '#e9ecef',
          'text-secondary': '#adb5bd',
          'border': '#495057',
        }
      },
      borderRadius: {
        'lg': '0.5rem',
      },
      transitionDuration: {
        '200': '200ms',
      }
    },
  },
  plugins: [],
}