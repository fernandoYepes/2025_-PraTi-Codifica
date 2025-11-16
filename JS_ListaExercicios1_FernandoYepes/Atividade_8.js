const prompt = require("prompt-sync")();

//Escreva um algoritmo para ler 2 valores (considere que não serão lidos valores iguais)
//e escreve-los em ordem crescente.

const valor1 = parseFloat(prompt("Digite o primeiro valor: "));
const valor2 = parseFloat(prompt("Digite o segundo valor (diferente do primeiro): "));

if (valor1 < valor2) {
  console.log(`Ordem crescente: ${valor1}, ${valor2}`);
} else {
  console.log(`Ordem crescente: ${valor2}, ${valor1}`);
}
