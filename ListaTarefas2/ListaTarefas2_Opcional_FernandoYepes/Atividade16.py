"""
16. Crie uma lógica que preencha um vetor de 20 posições com números aleatórios
(entre 0 e 99) gerados pelo computador. Logo em seguida, mostre os números gerados e
depois coloque o vetor em ordem crescente, mostrando no final os valores ordenados.
"""

import random

print("--- Vetor Aleatório e Ordenado ---")
print("Gerando 20 números aleatórios entre 0 e 99...")

vetor_aleatorio = []
LIMITE_POSICOES = 20

for i in range(LIMITE_POSICOES):
    numero = random.randint(0, 99)
    vetor_aleatorio.append(numero)

print("\n" + "=" * 30)
print("Vetor Original (desordenado):")
print(vetor_aleatorio)
print(f"(Total de {len(vetor_aleatorio)} números)")

vetor_aleatorio.sort()

print("\n" + "=" * 30)
print("Vetor Ordenado (ordem crescente):")
print(vetor_aleatorio)