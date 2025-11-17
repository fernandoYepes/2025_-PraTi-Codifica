"""
37. Escreva um algoritmo que leia um vetor G de 20 elementos caractere que representa
o gabarito de uma prova. A seguir, para cada um dos 50 alunos da turma, leia o vetor de
respostas (R) do aluno e conte o número de acertos. Mostre o número de acertos do
aluno e uma mensagem “APROVADO” se a quantidade de acertos for maior ou igual a 12;
e mostre uma mensagem de “REPROVADO”, caso contrário.
"""

import random

TAMANHO_PROVA = 20
NUM_ALUNOS = 50
NOTA_CORTE = 6
OPCOES = ['A', 'B', 'C', 'D']

gabarito = []

print("--- Gerando o Gabarito Oficial da Prova ---")
for i in range(TAMANHO_PROVA):
    gabarito.append(random.choice(OPCOES))

print(f"Gabarito: {gabarito}")
print("=" * 40)
print(f"--- Corrigindo as Provas dos {NUM_ALUNOS} Alunos ---")
print("=" * 40)

for i in range(NUM_ALUNOS):
    numero_aluno = i + 1
    respostas_aluno = []
    
    for j in range(TAMANHO_PROVA):
        respostas_aluno.append(random.choice(OPCOES))
        
    acertos = 0
    for k in range(TAMANHO_PROVA):
        if respostas_aluno[k] == gabarito[k]:
            acertos += 1
            
    print(f"Aluno Nº {numero_aluno:02d} | Acertos: {acertos:02d}", end=" -> ")
    
    if acertos >= NOTA_CORTE:
        print("APROVADO")
    else:
        print("REPROVADO")

print("=" * 40)
print("--- Correção Concluída ---")