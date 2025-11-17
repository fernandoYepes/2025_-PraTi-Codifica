"""
30. Escrever um algoritmo que lê uma matriz M(5,5) e cria 2 vetores SL(5) e SC(5) que
contenham, respectivamente, as somas das linhas e das colunas de M. Escrever a matriz
e os vetores criados.
"""

import random

TAMANHO = 5

matriz_M = []
vetor_SL = [0] * TAMANHO
vetor_SC = [0] * TAMANHO

print(f"--- Gerando Matriz Aleatória M {TAMANHO}x{TAMANHO} (números de 1 a 9) ---")

for i in range(TAMANHO):
    linha_atual = []
    for j in range(TAMANHO):
        numero = random.randint(1, 9)
        linha_atual.append(numero)
        
        vetor_SL[i] += numero
        vetor_SC[j] += numero
        
    matriz_M.append(linha_atual)


print("\n--- Matriz M Gerada ---")
for i in range(TAMANHO):
    for j in range(TAMANHO):
        print(f"[{matriz_M[i][j]}]", end=" ")
    print()

print("\n" + "=" * 40)
print("--- Vetor SL (Soma das Linhas) ---")
print(vetor_SL)

print("\n" + "=" * 40)
print("--- Vetor SC (Soma das Colunas) ---")
print(vetor_SC)