const prompt = require('prompt-sync')(); 

//Crie um programa que exibe a tabuada de um número fornecido pelo usuário (de 1 a
// 10) utilizando um loop for.

const numero = parseInt(prompt("Digite um número para ver a tabuada: "));

console.log(`\nTabuada do ${numero}:`);
for (let i = 1; i <= 10; i++) {
  console.log(`${numero} x ${i} = ${numero * i}`);
}
