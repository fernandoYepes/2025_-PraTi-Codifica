/*
Escreva um script que gere um número aleatório de 1 a 100 e peça ao
usuário, para adivinhar. Use while para repetir até acertar, contando
tentativas e exibindo “mais alto” ou “mais baixo” a cada palpite errado.
*/


function jogoDeAdivinhacaoBrowser() {
  const numeroSecreto = Math.floor(Math.random() * 100) + 1;

  // Inicializa Varivel
  let palpite = 0;
  let tentativas = 0;

  alert("--- Jogo de Adivinhar o Número ---\n Escolha entre 1 e 100, adivinhe!");

  // Loop
  while (palpite !== numeroSecreto) {
    const palpiteStr = prompt("Qual o seu palpite?");

    // Cancelar = jogo termina
    if (palpiteStr === null) {
      alert("Jogo cancelado.");
      return;
    }

    // Converter para número
    palpite = parseInt(palpiteStr);

    // Valida se é numero válido
    if (isNaN(palpite)) {
      alert("Entrada inválida! Digite apenas um número.");
      continue;
    }

    // Contador T
    tentativas++;

    if (palpite < numeroSecreto) {
      alert("Erroouuuuu! O número é mais alto. 🔼");
    } else if (palpite > numeroSecreto) {
      alert("Erroouuuuu! O número é mais baixo. 🔽");
    }
  }

  // Usuário acertou
  alert(`🎉 Parabéns! Você acertou o número ${numeroSecreto}!\n Você precisou de ${tentativas} tentativas.`);
}