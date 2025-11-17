"""
31. Escreva um algoritmo que leia um número inteiro A e uma matriz V 30 x 30 de inteiros.
Conte quantos valores iguais a A estão na matriz. Crie, a seguir, uma matriz X contendo
todos os elementos de V diferentes de A. Mostre os resultados.
"""

import random

LINHAS = 30
COLUNAS = 30

matriz_V = []
vetor_X = []
contador_A = 0

print(f"--- Gerando Matriz Aleatória V {LINHAS}x{COLUNAS} ---")
print("Aguarde, a matriz de 900 elementos está sendo criada...")

for i in range(LINHAS):
    linha_atual = []
    for j in range(COLUNAS):
        numero = random.randint(0, 10)
        linha_atual.append(numero)
    matriz_V.append(linha_atual)

print("Matriz V gerada com sucesso (não será exibida devido ao tamanho).")

while True:
    try:
        valor_A = int(input("\nDigite o valor A que deseja buscar (0-10): "))
        break
    except ValueError:
        print("Erro: Por favor, digite um NÚMERO INTEIRO.")

print(f"\nBuscando pelo valor {valor_A} e filtrando a matriz...")

for i in range(LINHAS):
    for j in range(COLUNAS):
        elemento_atual = matriz_V[i][j]
        
        if elemento_atual == valor_A:
            contador_A += 1
        else:
            vetor_X.append(elemento_atual)

print("\n" + "=" * 40)
print("--- RESULTADOS ---")
print("=" * 40)
print(f"O valor {valor_A} apareceu {contador_A} vezes na matriz V.")

print("\n--- Vetor X (elementos diferentes de A) ---")
print(f"O Vetor X foi criado com {len(vetor_X)} elementos.")
print(f"Os primeiros 50 elementos de X são:")
print(f"{vetor_X[:50]} ...")