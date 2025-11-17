"""
24. Dada uma matriz M[1..6,1..8], criar um vetor C que contenha, em cada posição, a
quantidade de elementos negativos da linha correspondente de M.
"""

import random

LINHAS_M = 6
COLUNAS_M = 8

matriz_M = []
vetor_C = []

print(f"--- Gerando Matriz Aleatória M {LINHAS_M}x{COLUNAS_M} ---")

for i in range(LINHAS_M):
    linha_atual = []
    for j in range(COLUNAS_M):
        numero = random.randint(-10, 10)
        linha_atual.append(numero)
    matriz_M.append(linha_atual)


print("Matriz M gerada:")
for linha in matriz_M:
    for elemento in linha:
        print(f"{elemento:4}", end="")
    print()

for linha in matriz_M:
    contador_negativos = 0
    for elemento in linha:
        if elemento < 0:
            contador_negativos += 1
    vetor_C.append(contador_negativos)

print("\n" + "=" * 40)
print("--- Vetor C (Contagem de Negativos por Linha) ---")
print("=" * 40)
print(vetor_C)