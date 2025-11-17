"""
28. Fazer um algoritmo para receber uma matriz 10 x 10 e devolver o resultado pedido no
item:
a) a soma dos elementos acima da diagonal principal;
b) a soma dos elementos abaixo da diagonal principal;
"""

import random

TAMANHO = 10
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

soma_acima_diagonal = 0.0
soma_abaixo_diagonal = 0.0

for i in range(TAMANHO):
    for j in range(TAMANHO):
        if j > i:
            soma_acima_diagonal += matriz[i][j]
        elif i > j:
            soma_abaixo_diagonal += matriz[i][j]

print("\n" + "=" * 40)
print("--- Resultado das Somas ---")
print("=" * 40)
print(f"a) Soma dos elementos ACIMA da diagonal principal: {soma_acima_diagonal}")
print(f"b) Soma dos elementos ABAIXO da diagonal principal: {soma_abaixo_diagonal}")