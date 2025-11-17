"""
36. Escreva um algoritmo que leia um vetor de 13 elementos inteiros, que é o Gabarito de
um teste da loteria esportiva. Leia, a seguir, para cada um dos 100 apostadores, o número
do seu cartão e um vetor de Respostas de 13 posições. Verifique para cada apostador o
número de acertos, comparando o vetor de Gabarito com o vetor de Respostas. Escreva
o número do apostador e o número de acertos. Se o apostador tiver 13 acertos, mostrar a
mensagem "Parabéns, tu foi o GANHADOR".
"""

import random

TAMANHO_VETOR = 13
NUM_APOSTADORES = 100

gabarito = []

print("--- Gerando o Gabarito da Loteria ---")
for i in range(TAMANHO_VETOR):
    gabarito.append(random.randint(1, 3))

print(f"Gabarito Oficial: {gabarito}")
print("=" * 40)
print(f"--- Verificando os {NUM_APOSTADORES} Apostadores ---")
print("=" * 40)

houve_ganhador = False

for i in range(NUM_APOSTADORES):
    numero_cartao = i + 1
    respostas_apostador = []
    
    for j in range(TAMANHO_VETOR):
        respostas_apostador.append(random.randint(1, 3))
        
    acertos = 0
    for k in range(TAMANHO_VETOR):
        if respostas_apostador[k] == gabarito[k]:
            acertos += 1
            
    print(f"Apostador Nº {numero_cartao:03d} | Acertos: {acertos:02d}")
    
    if acertos == TAMANHO_VETOR:
        print("!!! PARABÉNS, TU FOI O GANHADOR !!!")
        houve_ganhador = True

print("=" * 40)
print("--- Verificação Concluída ---")
if not houve_ganhador:
    print("Nenhum apostador gabaritou (13 acertos).")