const prompt = require('prompt-sync')();

//Escreva um programa que recebe um número inteiro e verifica se ele é par ou ímpar
//utilizando uma estrutura de controle if.

const numero = parseInt(prompt('Digite um NÚMERO: '));

if (numero % 2 === 0) {
    console.log(`${numero} é um número PAR!`);
} else {
    console.log(`${numero} é um número ÍMPAR!`);
}


