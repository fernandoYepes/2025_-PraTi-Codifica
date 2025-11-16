const prompt = require("prompt-sync")();

//Ler três valores para os lados de um triângulo: A, B e C. Verificar se os lados fornecidos
//formam realmente um triângulo. Caso forme, deve ser indicado o tipo de triângulo:
//Isósceles, escaleno ou eqüilátero.

// Verificar se os lados formam um triângulo
function Triangulo(A, B, C) {
    return (A < B + C) && (B < A + C) && (C < A + B);
}
function classificarTriangulo(A, B, C) {
    if (A === B && B === C) {
        return "Equilátero";  // Lados iguais
    } else if (A === B || A === C || B === C) {
        return "Isósceles";   // Dois lados iguais
    } else {
        return "Escaleno";    // Lados diferentes
    }
}

// Entra dados
console.log("\n=== VERIFICADOR DE TRIÂNGULO ===");
const triA = parseFloat(prompt("Digite o lado Triângulo A: "));
const triB = parseFloat(prompt("Digite o lado Triângulo B: "));
const triC = parseFloat(prompt("Digite o lado Triângulo C: "));

// Verificação e resultado
if (Triangulo(triA, triB, triC)) {
    const tipo = classificarTriangulo(triA, triB, triC);
    console.log(`\nOs lados formam um triângulo ${tipo}!`);
} else {
    console.log("\nOs lados NÃO formam um triângulo!");
}