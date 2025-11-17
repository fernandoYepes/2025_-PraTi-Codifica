"""
35. Elaborar um algoritmo que leia um conjunto de 30 valores e os coloca em 2 vetores
conforme forem pares ou ímpares. O tamanho do vetor é de 5 posições. Se algum vetor
estiver cheio, escrevê-lo. Terminada a leitura, escrever o conteúdo dos dois vetores. Cada
vetor pode ser preenchido quantas vezes forem necessárias.
"""

import random

TOTAL_VALORES = 30
TAMANHO_VETOR = 5

vetor_pares = []
vetor_impares = []

print(f"--- Lendo {TOTAL_VALORES} valores (Vetores de {TAMANHO_VETOR} posições) ---")

for i in range(TOTAL_VALORES):
    numero = random.randint(1, 100)
    print(f"Lido valor {i+1:2d}: {numero:3d}", end=" -> ")
    
    if numero % 2 == 0:
        vetor_pares.append(numero)
        print("Adicionado aos PARES.")
        
        if len(vetor_pares) == TAMANHO_VETOR:
            print(f"!! VETOR DE PARES CHEIO: {vetor_pares}")
            vetor_pares = []
    else:
        vetor_impares.append(numero)
        print("Adicionado aos ÍMPARES.")
        
        if len(vetor_impares) == TAMANHO_VETOR:
            print(f"!! VETOR DE ÍMPARES CHEIO: {vetor_impares}")
            vetor_impares = []

print("\n" + "=" * 40)
print("--- LEITURA DOS 30 VALORES TERMINADA ---")
print("Escrevendo conteúdo restante (sobras) dos vetores:")
print("=" * 40)

if len(vetor_pares) > 0:
    print(f"VETOR DE PARES (SOBRA): {vetor_pares}")
else:
    print("VETOR DE PARES (SOBRA): Vazio.")

if len(vetor_impares) > 0:
    print(f"VETOR DE ÍMPARES (SOBRA): {vetor_impares}")
else:
    print("VETOR DE ÍMPARES (SOBRA): Vazio.")