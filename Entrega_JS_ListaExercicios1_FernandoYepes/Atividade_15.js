let n1 = 0;
let n2 = 1;

//Escreva um programa que gera e imprime os primeiros 10 números da sequência de
//Fibonacci utilizando um loop for.

console.log("Sequência de Fibonacci (10 primeiros números):");
for (let i = 0; i < 10; i++) {
  console.log(n1);
  let proximo = n1 + n2;
  n1 = n2;
  n2 = proximo;
}
