/**
 * Escreva duas funções:

○ paresParaObjeto(pares) recebe um array de pares [ [chave,
valor], ... ] e retorna o objeto equivalente.
○ objetoParaPares(obj) faz o inverso, retornando um array de
pares.

 * Converte um array de pares [chave, valor] em um objeto
 * @param {Array<[string, any]>} 
 * @returns {Object} 
 */
function paresParaObjeto(pares) {
  return Object.fromEntries(pares);
}


/**
 * Converte em array de pares (chave, valor)
 * @param {Object} obj
 * @returns {Array<[string, any]>}
 */
function objetoParaPares(obj) {
  // Object.entries() conversão direta
  return Object.entries(obj);
}