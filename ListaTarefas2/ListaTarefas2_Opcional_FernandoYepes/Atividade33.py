"""
33. Faça um algoritmo que leia uma matriz 3 x 3 e após a leitura, multiplique os
elementos da diagonal principal com a média dos elementos da diagonal secundária.
"""

import random

TAMANHO = 3
matriz = []

print(f"--- Gerando Matriz Aleatória M {TAMANHO}x{TAMANHO} (números de 1 a 9) ---")

for i in range(TAMANHO):
    linha_atual = []
    for j in range(TAMANHO):
        numero = random.randint(1, 9)
        linha_atual.append(numero)
    matriz.append(linha_atual)

print("\n--- Matriz Original ---")
for i in range(TAMANHO):
    for j in range(TAMANHO):
        print(f"[{matriz[i][j]}]", end=" ")
    print()

soma_diagonal_secundaria = 0.0
for i in range(TAMANHO):
    soma_diagonal_secundaria += matriz[i][(TAMANHO - 1) - i]

media_diagonal_secundaria = soma_diagonal_secundaria / TAMANHO

print("\n" + "=" * 40)
print(f"Soma da Diagonal Secundária: {soma_diagonal_secundaria}")
print(f"Média da Diagonal Secundária: {media_diagonal_secundaria:.2f}")
print("=" * 40)

print("\nMultiplicando a Diagonal Principal pela média...")

for i in range(TAMANHO):
    matriz[i][i] = matriz[i][i] * media_diagonal_secundaria

print("\n--- Matriz Modificada ---")
for i in range(TAMANHO):
    for j in range(TAMANHO):
        if i == j:
            print(f"[{matriz[i][j]:6.2f}]", end=" ")
        else:
            print(f"[ {matriz[i][j]:<4} ]", end=" ")
    print()