const prompt = require('prompt-sync')();

while (true) {
  console.log('\n=== MENU  ===');
  console.log('1. Dizer "Olá"');
  console.log('2. Contar até 3');
  console.log('3. Sair');

  const opcao = prompt('Escolha uma opção: ');

  switch (opcao) {
    case '1':
      console.log('Olá! Tudo bem?');
      break;

    case '2':
      console.log('1.. 2.. 3!');
      break;

    case '3':
      console.log('Até logo!');
      process.exit();

    default:
      console.log('Opção inválida!');
  }
}1