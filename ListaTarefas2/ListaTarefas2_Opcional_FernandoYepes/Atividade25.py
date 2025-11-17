"""
25. Faça um algoritmo que leia uma matriz de 15 X 20 de números reais e mostre a soma
de cada coluna separadamente.
"""

import random

LINHAS = 15
COLUNAS = 20

matriz = []

for i in range(LINHAS):
    linha_atual = []
    for j in range(COLUNAS):
        numero = random.uniform(0, 10)
        linha_atual.append(numero)
    matriz.append(linha_atual)

print(f"--- Matriz {LINHAS}x{COLUNAS} Gerada (números de 0.0 a 10.0) ---")
for linha in matriz:
    for elemento in linha:
        print(f"{elemento:5.1f}", end="")
    print()


vetor_soma_colunas = [0.0] * COLUNAS

for i in range(LINHAS):
    for j in range(COLUNAS):
        vetor_soma_colunas[j] += matriz[i][j]

print("\n" + "=" * 40)
print("--- Soma de Cada Coluna ---")
print("=" * 40)

for j in range(COLUNAS):
    print(f"Soma da Coluna {j}: \t{vetor_soma_colunas[j]:.2f}")