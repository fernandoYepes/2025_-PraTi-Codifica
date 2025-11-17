/*
Crie function debounce(fn, delay) que receba uma função fn e um delay
em ms, retornando uma nova função que só executa fn se não for
chamada novamente dentro do intervalo.
*/

/**
  @param {Function} fn Será "debounced"
  @param {number} delay 
  @returns {Function}
 */

function debounce(fn, delay) {
  let timeoutId;

  // Retorna nova função
  return function(...args) {
    // Guarda o contexto 'this'
    const context = this;

    // Cancela o timer anterior. Se a função for chamada novamente dentro do 'delay'
    clearTimeout(timeoutId);

    // Cria um NOVO timer
    timeoutId = setTimeout(() => {
      // timer = completo, executa (fn)
      fn.apply(context, args);
    }, delay);
  };
}