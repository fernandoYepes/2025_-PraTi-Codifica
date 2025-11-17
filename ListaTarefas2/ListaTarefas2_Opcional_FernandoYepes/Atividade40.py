"""
40. Faça um algoritmo que leia um vetor de 5 elementos inteiros, correspondentes ao
resultado oficial da Loto. A seguir, leia 50 conjuntos de vetores (com 5 elementos inteiros
cada), representando as apostas feitas. Compare os números das apostas com o
resultado oficial e mostre uma mensagem ("Ganhador") se todos os números
corresponderem ao resultado oficial. (Observação: não é necessário procurar por ternos
e quadras, apenas por quinas.)
"""

import random

TAMANHO_APOSTA = 5
NUM_APOSTADORES = 50
NUMERO_MIN = 1
NUMERO_MAX = 60

gabarito_loto = []
apostas = []

print("--- Gerando o Resultado Oficial da Loto ---")

while len(gabarito_loto) < TAMANHO_APOSTA:
    numero = random.randint(NUMERO_MIN, NUMERO_MAX)
    if numero not in gabarito_loto:
        gabarito_loto.append(numero)
        
gabarito_loto.sort()
print(f"Resultado Oficial: {gabarito_loto}")

print("\n" + "=" * 40)
print(f"--- Verificando as {NUM_APOSTADORES} Apostas ---")
print("=" * 40)

houve_ganhador = False

for i in range(NUM_APOSTADORES):
    numero_cartao = i + 1
    aposta_atual = []
    
    while len(aposta_atual) < TAMANHO_APOSTA:
        numero_apostado = random.randint(NUMERO_MIN, NUMERO_MAX)
        if numero_apostado not in aposta_atual:
            aposta_atual.append(numero_apostado)
    
    aposta_atual.sort()
    
    acertos = 0
    for numero in aposta_atual:
        if numero in gabarito_loto:
            acertos += 1
            
    if acertos == TAMANHO_APOSTA:
        print(f"Apostador Nº {numero_cartao:02d} | Aposta: {aposta_atual} | Acertos: {acertos} -> GANHADOR")
        houve_ganhador = True
    else:
        pass

print("=" * 40)
print("--- Verificação Concluída ---")
if not houve_ganhador:
    print("Nenhum apostador fez a quina (5 acertos).")