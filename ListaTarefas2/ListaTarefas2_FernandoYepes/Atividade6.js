/**
    Implemente function memoize(fn) que armazene em cache chamadas
    anteriores de fn (por argumentos), retornando resultados instantâneos em
    repetidas invocações.
 */
/**
    @param {Function} fn A função original a ser otimizada
    @returns {Function} Uma nova função com capacidade de cache
 */

    function memoize(fn) {
  const cache = {};

  // função otimizada..
  return function(...args) {
    // JSON.stringify converte array de argumentos em string única
    const key = JSON.stringify(args);

    // Verifica se o resultado para cache
    if (key in cache) {
      console.log(`Procurando do cache para os argumentos: ${key}`);
      return cache[key];
    }
    else {
      // Exe função original
      console.log(`Executando cálculo para os argumentos: ${key}`);
      const result = fn(...args);

      // Armazena o novo resultado
      cache[key] = result;

      return result;
    }
  };
}