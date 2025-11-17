"""
15. Desenvolva um programa que leia 10 números inteiros e guarde-os em um vetor. No
final, mostre quais são os números pares que foram digitados e em que posições eles
estão armazenados.
"""

print("--- Detector de Números Pares e Posições ---")

vetor_numeros = []

print("Por favor, digite 10 números inteiros:")

for i in range(10):
    while True:
        try:
            numero_str = input(f"Digite o {i + 1}º número: ")
            numero_int = int(numero_str)
            vetor_numeros.append(numero_int)
            break
        except ValueError:
            print("Erro: Por favor, digite apenas um NÚMERO INTEIRO (ex: 4 ou -2).")

print("\n" + "=" * 30)
print("--- Análise dos Números Pares ---")
print("=" * 30)

encontrou_par = False

for indice, numero in enumerate(vetor_numeros):
    if numero % 2 == 0:
        print(f"Número PAR {numero} encontrado na Posição {indice}")
        encontrou_par = True

if not encontrou_par:
    print("Nenhum número par foi digitado.")