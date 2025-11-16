const prompt = require("prompt-sync")();

//Implemente um programa que recebe uma nota de 0 a 10 e classifica como
//"Aprovado", "Recuperação", ou "Reprovado" utilizando if-else if.

const nota = parseFloat(prompt('Digite a nota (0 a 10): '));

if (isNaN(nota)) {
    console.log('Erro: Digite apenas números!');
} else if (nota < 0 || nota > 10) {
    console.log('Erro: A nota deve estar entre 0 e 10!');
} else if (nota >= 7) {
    console.log('Aprovado! 👍');
} else if (nota >= 5) {
    console.log('Recuperação!');
} else {
    console.log('Reprovado. 😭');
}