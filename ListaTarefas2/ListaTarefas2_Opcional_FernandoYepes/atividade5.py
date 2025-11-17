"""
5. Crie um jogo de JoKenPo (Pedra-Papel-Tesoura).
"""

import random

# importar 'time' para dar um efeito "dramático"
import time

print("--- Vamos Jogar JoKenPo! ---")

opcoes = ['pedra', 'papel', 'tesoura']

# Coletar a escolha do usuário
usuario_escolha = input("Escolha Pedra, Papel ou Tesoura: ").lower().strip()

if usuario_escolha not in opcoes:
    print(f"\nErro: '{usuario_escolha}' não é uma opção válida.")
    print("Por favor, escolha apenas 'pedra', 'papel' ou 'tesoura'.")
else:
    # computador faz a escolha dele
    computador_escolha = random.choice(opcoes)

    print("\nJO...")
    time.sleep(0.5) 
    print("KEN...")
    time.sleep(0.5)
    print("PO!")
    time.sleep(0.5)

    print("-" * 30)
    print(f"Você escolheu: {usuario_escolha.upper()}")
    print(f"O computador escolheu: {computador_escolha.upper()}")
    print("-" * 30)
    
    if usuario_escolha == computador_escolha:
        # Empate
        print("Resultado: É um EMPATE!")
        

    elif (usuario_escolha == 'pedra' and computador_escolha == 'tesoura') or \
         (usuario_escolha == 'papel' and computador_escolha == 'pedra') or \
         (usuario_escolha == 'tesoura' and computador_escolha == 'papel'):
        # Usuário Vence
        print("Resultado: Você VENCEU! Parabéns!")
        

    else:
        # vitória do Computador
        print("Resultado: Você PERDEU! O computador venceu.")