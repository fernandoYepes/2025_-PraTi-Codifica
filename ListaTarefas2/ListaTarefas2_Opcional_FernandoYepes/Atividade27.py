"""
27. Elaborar um algoritmo que leia uma matriz M(6,6) e um valor A. Após a leitura,
multiplicar a matriz M pelo valor A e colocar os valores da matriz multiplicados por A em
um vetor V(36). Escrever o vetor V no final.
"""

import random

LINHAS = 6
COLUNAS = 6
TOTAL_ELEMENTOS = LINHAS * COLUNAS

matriz_M = []
vetor_V = []

print(f"--- Gerando Matriz Aleatória M {LINHAS}x{COLUNAS} ---")

for i in range(LINHAS):
    linha_atual = []
    for j in range(COLUNAS):
        numero = random.randint(1, 10)
        linha_atual.append(numero)
    matriz_M.append(linha_atual)

print("Matriz M gerada:")
for linha in matriz_M:
    for elemento in linha:
        print(f"[{elemento:2}]", end=" ")
    print()

while True:
    try:
        valor_A = float(input("\nDigite o valor multiplicador (A): "))
        break
    except ValueError:
        print("Erro: Por favor, digite um número válido (ex: 2 ou 1.5).")

print(f"\nMultiplicando a Matriz M pelo valor A ({valor_A})...")

for i in range(LINHAS):
    for j in range(COLUNAS):
        valor_multiplicado = matriz_M[i][j] * valor_A
        vetor_V.append(valor_multiplicado)

print("\n" + "=" * 40)
print(f"--- Vetor V ({TOTAL_ELEMENTOS} elementos) ---")
print("=" * 40)
print(vetor_V)