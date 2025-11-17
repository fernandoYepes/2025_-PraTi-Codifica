"""
38. Elabore um algoritmo que leia um vetor de 6 posições e após sua leitura leia outra
variável identificadora que calcule a operação conforme a informação contida nesta
variável:
1- soma dos elementos;
2- produto dos elementos;
3- média dos elementos;
4- ordene os elementos em ordem crescente;
5- mostre o vetor.
"""

import math

TAMANHO_VETOR = 6
vetor = []

print(f"--- Leitura de Vetor de {TAMANHO_VETOR} posições ---")
print(f"Por favor, digite {TAMANHO_VETOR} números.")

for i in range(TAMANHO_VETOR):
    while True:
        try:
            numero_str = input(f"Digite o {i + 1}º número: ")
            numero = float(numero_str)
            vetor.append(numero)
            break
        except ValueError:
            print("Erro: Por favor, digite um NÚMERO válido.")

print("\nVetor lido:")
print(vetor)

print("\n" + "=" * 40)
print("--- Escolha a Operação ---")
print("1: Soma dos elementos")
print("2: Produto dos elementos")
print("3: Média dos elementos")
print("4: Ordenar (ordem crescente)")
print("5: Mostrar o vetor original")
print("=" * 40)

while True:
    try:
        operacao = int(input("Digite o código da operação (1-5): "))
        if 1 <= operacao <= 5:
            break
        else:
            print("Erro: Código inválido. Digite um número entre 1 e 5.")
    except ValueError:
        print("Erro: Por favor, digite um NÚMERO INTEIRO.")

print("\n--- Resultado da Operação ---")

if operacao == 1:
    soma_elementos = sum(vetor)
    print(f"1 - SOMA: {soma_elementos}")

elif operacao == 2:
    produto_elementos = 1
    for num in vetor:
        produto_elementos *= num
    print(f"2 - PRODUTO: {produto_elementos}")

elif operacao == 3:
    media_elementos = sum(vetor) / len(vetor)
    print(f"3 - MÉDIA: {media_elementos:.2f}")

elif operacao == 4:
    vetor.sort()
    print("4 - ORDENADO (crescente):")
    print(vetor)

elif operacao == 5:
    print("5 - VETOR ORIGINAL:")
    print(vetor)