const prompt = require('prompt-sync')(); // Importa o prompt para entrada

//Escreva um programa que solicita ao usuário 5 números e calcula a soma total
//utilizando um loop for.

let soma = 0; 

for (let i = 1; i <= 5; i++) {
  const numero = parseFloat(prompt(`Digite o ${i}º número: `));
  soma += numero;
}

console.log(`A soma total dos 5 números é: ${soma}`);
