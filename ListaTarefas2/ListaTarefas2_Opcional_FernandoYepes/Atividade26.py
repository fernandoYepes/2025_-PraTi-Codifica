"""
26. Dadas duas matrizes numéricas A[1..3,1..5] e B[1..3,1..5], calcular a matriz produto
P[1..3,1..5].
"""

import random

LINHAS = 3
COLUNAS = 5

matriz_A = []
matriz_B = []
matriz_P = []

print(f"--- Gerando Matrizes Aleatórias A e B ({LINHAS}x{COLUNAS}) ---")

for i in range(LINHAS):
    linha_a = []
    for j in range(COLUNAS):
        linha_a.append(random.randint(1, 9))
    matriz_A.append(linha_a)

for i in range(LINHAS):
    linha_b = []
    for j in range(COLUNAS):
        linha_b.append(random.randint(1, 9))
    matriz_B.append(linha_b)

print("\n--- Matriz A ---")
for linha in matriz_A:
    for elemento in linha:
        print(f"[{elemento}]", end=" ")
    print()

print("\n--- Matriz B ---")
for linha in matriz_B:
    for elemento in linha:
        print(f"[{elemento}]", end=" ")
    print()

for i in range(LINHAS):
    linha_p = []
    for j in range(COLUNAS):
        produto_elemento = matriz_A[i][j] * matriz_B[i][j]
        linha_p.append(produto_elemento)
    matriz_P.append(linha_p)

print("\n" + "=" * 40)
print("--- Matriz P (Produto A[i,j] * B[i,j]) ---")
print("=" * 40)
for linha in matriz_P:
    for elemento in linha:
        print(f"[{elemento:4}]", end=" ")
    print()