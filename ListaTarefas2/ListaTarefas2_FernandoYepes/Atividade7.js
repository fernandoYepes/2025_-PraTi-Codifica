/*
Dado um array produtos = [{ nome, preco }, ...], crie uma função que
retorne um novo array apenas com os nomes, ordenados por preço
crescente, usando map, sort.
*/

/**
 * Retorna um novo array, preço em ordem crescente
 *
 * @param {Array<Object>} produtos
 * @returns {Array<string>} Array com os nomes dos produtos
 */
function ordenarNomesPorPreco(produtos) {
  // .sort() modifica array original
  const produtosCopiados = [...produtos];

  // Se for positivo, 'b' vem antes de 'a'
  const produtosOrdenados = produtosCopiados.sort((a, b) => a.preco - b.preco);

  // .map() extrai nomes e cria novo array
  const nomes = produtosOrdenados.map(produto => produto.nome);

  // Retorna array final
  return nomes;
}