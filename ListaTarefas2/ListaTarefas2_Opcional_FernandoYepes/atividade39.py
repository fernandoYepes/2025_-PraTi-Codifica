"""
39. Faça um algoritmo que leia um vetor (A) de 100 posições. Em seguida, compacte o
vetor, retirando os valores nulos e negativos. Coloque o resultado no vetor B.
"""

import random

TAMANHO_A = 100
vetor_A = []
vetor_B = []

print(f"--- Gerando Vetor A de {TAMANHO_A} posições ---")
print("Valores aleatórios entre -10 e 10 serão usados.")

for i in range(TAMANHO_A):
    vetor_A.append(random.randint(-10, 10))

print("Vetor A gerado (não será exibido devido ao tamanho).")

for i in range(TAMANHO_A):
    elemento_atual = vetor_A[i]
    
    if elemento_atual > 0:
        vetor_B.append(elemento_atual)

print("\n" + "=" * 40)
print("--- Vetor B (Compactado, apenas positivos) ---")
print("=" * 40)
print(f"O Vetor B foi criado com {len(vetor_B)} elementos.")
print(vetor_B)