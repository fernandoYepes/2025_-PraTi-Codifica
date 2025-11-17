"""
32. Escrever um algoritmo que lê uma matriz M(12,13) e divida todos os 13 elementos de
cada uma das 12 linhas de M pelo maior elemento em módulo daquela linha. Escrever a
matriz lida e a modificada.
"""

import random

LINHAS = 12
COLUNAS = 13

matriz_M = []
matriz_modificada = []

print(f"--- Gerando Matriz Aleatória M {LINHAS}x{COLUNAS} ---")
print("Valores aleatórios entre -10 e 10 serão usados.")

for i in range(LINHAS):
    linha_atual = []
    for j in range(COLUNAS):
        numero = random.randint(-10, 10)
        linha_atual.append(numero)
    matriz_M.append(linha_atual)

print("\n" + "=" * 50)
print("--- Matriz Lida (Original) ---")
print("=" * 50)
for i in range(LINHAS):
    for j in range(COLUNAS):
        print(f"[{matriz_M[i][j]:4}]", end=" ")
    print()

for i in range(LINHAS):
    linha_original = matriz_M[i]
    
    maior_em_modulo = 0
    for elemento in linha_original:
        if abs(elemento) > maior_em_modulo:
            maior_em_modulo = abs(elemento)
            
    linha_nova = []
    
    if maior_em_modulo == 0:
        linha_nova = [0.0] * COLUNAS
    else:
        for elemento in linha_original:
            linha_nova.append(elemento / maior_em_modulo)
            
    matriz_modificada.append(linha_nova)

print("\n" + "=" * 50)
print("--- Matriz Modificada (Normalizada por linha) ---")
print("=" * 50)
for i in range(LINHAS):
    for j in range(COLUNAS):
        print(f"[{matriz_modificada[i][j]:6.2f}]", end=" ")
    print()