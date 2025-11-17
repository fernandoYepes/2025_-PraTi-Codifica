"""
29. Escreva um algoritmo que leia uma matriz M(5,5) e calcule as somas:
a) da linha 4 de M;
b) da coluna 2 de M;
c) da diagonal principal;
d) todos os elementos da matriz M.
Escrever essas somas e a matriz.
"""

import random

TAMANHO = 5
matriz = []

print(f"--- Gerando Matriz Aleatória M {TAMANHO}x{TAMANHO} (números de 1 a 9) ---")

for i in range(TAMANHO):
    linha_atual = []
    for j in range(TAMANHO):
        numero = random.randint(1, 9)
        linha_atual.append(numero)
    matriz.append(linha_atual)

print("Matriz M gerada:")
for i in range(TAMANHO):
    for j in range(TAMANHO):
        print(f"[{matriz[i][j]}]", end=" ")
    print()

soma_linha_4 = 0.0
soma_coluna_2 = 0.0
soma_diagonal_principal = 0.0
soma_total = 0.0

LINHA_ALVO = 3
COLUNA_ALVO = 1

for i in range(TAMANHO):
    for j in range(TAMANHO):
        
        elemento_atual = matriz[i][j]
        
        soma_total += elemento_atual
        
        if i == LINHA_ALVO:
            soma_linha_4 += elemento_atual
            
        if j == COLUNA_ALVO:
            soma_coluna_2 += elemento_atual
            
        if i == j:
            soma_diagonal_principal += elemento_atual

print("\n" + "=" * 40)
print("--- Resultado das Somas ---")
print("=" * 40)
print(f"a) Soma da Linha 4 (índice 3): {soma_linha_4}")
print(f"b) Soma da Coluna 2 (índice 1): {soma_coluna_2}")
print(f"c) Soma da Diagonal Principal: {soma_diagonal_principal}")
print(f"d) Soma Total de todos os elementos: {soma_total}")