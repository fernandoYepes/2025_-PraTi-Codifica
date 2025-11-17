/*
Crie a função ehDataValida(dia, mes, ano) que retorne true se os valores
formarem uma data real (meses de 28–31 dias, ano bissexto para
fevereiro) e false caso contrário.
*/

/**
  @param {number} dia Dia escolhido
  @param {number} mes Mês escolhido
  @param {number} ano Ano escolhido
  @returns {boolean} 
 */

function ehDataValidaV2(dia, mes, ano) {
  dia = parseInt(dia, 10);
  mes = parseInt(mes, 10);
  ano = parseInt(ano, 10);

  // Se a conversão resultar em NaN, é inválido
  if (isNaN(dia) || isNaN(mes) || isNaN(ano)) {
    return false;
  }
  
  const data = new Date(ano, mes - 1, dia);

  // Se o JS ajustou a data (ex: dia 32 virou dia 1 do mês seguinte), valor muda
  return (
    data.getFullYear() === ano &&
    data.getMonth() === mes - 1 &&
    data.getDate() === dia
  );
}