/*
Implemente function fatorial(n) de forma recursiva; trate n < 0 lançando
um Error, e n === 0 retornando 1.
*/

/**
 * Calcula o fatorial de um número (n!), forma recursiva
 * * @param {number} n 
 * @returns {number} 
 * @throws {Error} Da um erro se n for um número negativo
 */

function fatorial(n) {
  // Tratar erro
  if (n < 0) {
    throw new Error("Não definido para números negativos.");
  }

  // Fatorial de 0 = 1.
  if (n === 0) {
    return 1;
  }

  // mesma função com valor menor
  else {
    return n * fatorial(n - 1);
  }
}