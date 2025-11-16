const prompt = require("prompt-sync")();

//As maçãs custam R$ 0,30 se forem compradas menos do que uma dúzia, e R$ 0,25 se
//forem compradas pelo menos doze. Escreva um algoritmo que leia o número de maçãs
//compradas, calcule e escreva o valor total da compra.

const quantidade = parseInt(prompt("Digite o número de maçãs compradas: "));

let precoPorUnidade;

if (quantidade >= 12) {
  precoPorUnidade = 0.25;
} else {
  precoPorUnidade = 0.30;
}

const total = quantidade * precoPorUnidade;

console.log(`O valor total da compra é R$ ${total.toFixed(2)}`);