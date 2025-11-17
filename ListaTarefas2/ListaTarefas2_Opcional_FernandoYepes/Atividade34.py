"""
34. Faça um algoritmo que leia uma matriz 50 x 50 de números reais. A seguir, multiplique
cada linha pelo elemento da diagonal principal daquela linha. Mostre a matriz após as
multiplicações.
"""

import random

TAMANHO = 5
matriz = []

print(f"--- Gerando Matriz Aleatória M {TAMANHO}x{TAMANHO} (números de 1 a 5) ---")

for i in range(TAMANHO):
    linha_atual = []
    for j in range(TAMANHO):
        numero = random.randint(1, 5)
        linha_atual.append(numero)
    matriz.append(linha_atual)

print("\n--- Matriz Original ---")
for i in range(TAMANHO):
    for j in range(TAMANHO):
        print(f"[{matriz[i][j]:2}]", end=" ")
    print()

vetor_diagonal_principal = []
for i in range(TAMANHO):
    vetor_diagonal_principal.append(matriz[i][i])

print("\n" + "=" * 40)
print(f"Elementos da Diagonal Principal (Multiplicadores):")
print(vetor_diagonal_principal)
print("=" * 40)

print("\nMultiplicando cada linha pelo seu elemento da diagonal...")

matriz_modificada = []
for i in range(TAMANHO):
    linha_original = matriz[i]
    multiplicador = vetor_diagonal_principal[i]
    
    linha_nova = []
    for j in range(TAMANHO):
        novo_valor = linha_original[j] * multiplicador
        linha_nova.append(novo_valor)
        
    matriz_modificada.append(linha_nova)

print("\n--- Matriz Modificada ---")
for i in range(TAMANHO):
    for j in range(TAMANHO):
        print(f"[{matriz_modificada[i][j]:4}]", end=" ")
    print()