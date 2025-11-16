const prompt = require("prompt-sync")();

// Escreva um programa que calcula o Índice de Massa Corporal (IMC) de uma pessoa e
//determina a categoria de peso (baixo peso, peso normal, sobrepeso, obesidade)
//utilizando if-else.

function classificarIMC(imc) {
    if (imc < 18.5) return "Baixo peso";
    else if (imc < 25) return "Peso normal";
    else if (imc < 30) return "Sobrepeso";
    else return "Obesidade";
}

// Validar entrada numérica
function lerDado(mensagem) {
    let valor;
    do {
        valor = parseFloat(prompt(mensagem));
        if (isNaN(valor)) console.log("Erro: Digite um número válido!");
    } while (isNaN(valor));
    
    return valor;
}

// Principal
console.log("\n=== CALCULADORA DE IMC ===");
const peso = lerDado("Peso (kg): ");
const altura = lerDado("Altura (m): ");
const imc = peso / (altura ** 2);

console.log(`\nSeu IMC é ${imc.toFixed(1)} - ${classificarIMC(imc)}`);