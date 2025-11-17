/**
 * Em vendas = [{ cliente, total }, ...], use reduce para gerar um objeto onde
cada chave é um cliente e o valor é a soma de todos os seus total.
 *
 * @param {Array<Object>} vendas Um array de objetos de venda
 * @returns {Object} Um objeto onde as chaves são os nomes dos clientes e os valores são a soma de seus totais
 */
function agruparVendasPorCliente(vendas) {
  // O método .reduce() tem função "redutora" = único valor de retorno
  return vendas.reduce((acumulador, vendaAtual) => {
    // Para cada item 'vendaAtual'
    const cliente = vendaAtual.cliente;

    // Verifica se  cliente
    if (acumulador[cliente]) {
      // Se já existe, soma o 'total' da venda atual ao valor existente
      acumulador[cliente] += vendaAtual.total;
    } else {
      acumulador[cliente] = vendaAtual.total;
    }

    // Retorna o acumulador modificado
    return acumulador;

  }, {}); // Valor inicial
}