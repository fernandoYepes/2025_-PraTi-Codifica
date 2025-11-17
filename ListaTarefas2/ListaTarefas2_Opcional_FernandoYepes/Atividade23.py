"""
23. Criar e imprimir a matriz identidade MI[1..7,1..7] em que todos os elementos da
diagonal principal são iguais a 1 e os demais são nulos.
"""

print("--- Matriz Identidade 7x7 ---")

TAMANHO = 7
matriz_identidade = []

for i in range(TAMANHO):
    
    linha_atual = []
    
    for j in range(TAMANHO):
        
        if i == j:
            linha_atual.append(1)
        else:
            linha_atual.append(0)
            
    matriz_identidade.append(linha_atual)

print(f"\nMatriz Identidade {TAMANHO}x{TAMANHO} gerada:")

for linha in matriz_identidade:
    for elemento in linha:
        print(f"{elemento}", end=" ")
    print()