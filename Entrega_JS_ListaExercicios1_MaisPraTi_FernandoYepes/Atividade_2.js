const prompt = require("prompt-sync")();

//Crie um programa que classifica a idade de uma pessoa em categorias (criança,
//adolescente, adulto, idoso) com base no valor fornecido, utilizando uma estrutura de
//controle if-else.

const idade = parseInt(prompt('Digite a idade: '));

if (isNaN(idade)) {
    console.log('Por favor, digite um número válido!');
} else if (idade < 0) {
    console.log('Idade inválida!');
} else if (idade <= 11) {
    console.log('Criança (0-11 anos)');
} else if (idade <= 13) {
    console.log('Adolescente (12-13 anos)');
} else if (idade <= 17) {
    console.log('Jovem Adulto (14-17 anos)');
} else if (idade <= 59) {
    console.log('Adulto (18-59 anos)');
} else {
    console.log('Idoso (60+ anos)');
}
