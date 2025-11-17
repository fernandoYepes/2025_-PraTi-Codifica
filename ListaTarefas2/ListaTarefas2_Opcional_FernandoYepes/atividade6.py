"""
6. Crie um jogo onde o computador vai sortear um número entre 1 e 5. O jogador vai
tentar descobrir qual foi o valor sorteado.
"""

# Importar a função 'randint' do módulo 'random'
# randint = "random integer" (inteiro aleatório)
import random

import time

print("--- Jogo de Adivinhação ---")
print("Vou pensar em um número entre 1 e 5. Tente adivinhar!")
print("-" * 30)

# random.randint(1, 5) sorteia um número inteiro, incluindo o 1 e o 5.
numero_secreto = random.randint(1, 5)

# Dando um tempo para o computador "pensar"
time.sleep(1)
print("Pensei...")
time.sleep(0.5)

try:
    #  Pergunta palpite do jogador
    palpite = int(input("Qual número eu pensei? "))
    print("-" * 30)

    #  Validar
    if palpite < 1 or palpite > 5:
        print(f"Erro: O seu palpite ({palpite}) não está entre 1 e 5.")
        print("Você perdeu sua chance!")
    else:
        #  Lógica para verificar se o jogador acertou
        if palpite == numero_secreto:
            
            print(f"BOA! Você acertou! Eu realmente pensei no número {numero_secreto}.")
        else:
            
            print(f"Que pena, você errou. O número que eu pensei foi o {numero_secreto}.")

except ValueError:
    print("\nErro: Você deveria ter digitado um NÚMERO (como 1, 2, 3...).")
    print("Você perdeu sua chance!")