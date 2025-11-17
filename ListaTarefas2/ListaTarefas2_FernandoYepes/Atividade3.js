/*
Dada uma string (ex.: "olá olá mundo mundo"), use if/else e for para extrair
todas as palavras únicas e exibi-las em um array.
*/

/**
  Extrai palavras de uma string
  @param {string} frase A string de entrada para processar
  @returns {string[]} Um array contendo apenas as palavras únicas
 */

function extrairPalavrasUnicas(frase) {
  // Converte
  const palavras = frase.toLowerCase().split(' ');

  // Armazena
  const palavrasUnicas = [];

  // Loop for
  for (const palavra of palavras) {
    
    // retorna 'true' se o array contém o elemento
    if (!palavrasUnicas.includes(palavra)) {
      palavrasUnicas.push(palavra);
    } else {
      // Palavra já está no array, loop continua
    }
  }

  return palavrasUnicas;
}