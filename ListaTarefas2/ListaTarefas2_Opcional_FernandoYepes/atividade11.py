"""
11. Desenvolva um programa que leia o primeiro termo e a razão de uma PA (Progressão
Aritmética), mostrando na tela os 10 primeiros elementos da PA e a soma entre todos os
valores da sequência.
"""
55
print("--- Calculadora de Progressão Aritmética (PA) ---")

try:
    # Usamos float() para permitir PAs com números decimais
    primeiro_termo = float(input("Digite o primeiro termo (a1): "))
    razao = float(input("Digite a razão (r): "))
    
    print("-" * 30)
    print(f"PA com a1 = {primeiro_termo} e r = {razao}")
    print("Os 10 primeiros termos são:")
    
    # Inicializar as variáveis
    soma_total = 0.0
    termo_atual = primeiro_termo
    
    # O range(10) vai de 0 a 9 (executando 10 vezes)
    for i in range(10):
        
        # Mostrar o termo atual
        # O 'end=" -> "' faz o print não quebrar a linha
        print(f"{termo_atual}", end=" -> ")
        
        # Acumular o valor na soma
        soma_total += termo_atual
        
        # Calcular o próximo termo
        termo_atual += razao
        
    # Finalizar a linha e mostrar a soma
    print("FIM") # Quebra a linha após o '->'
    
    print("-" * 30)
    print(f"A soma de todos os 10 valores é: {soma_total:.2f}")

except ValueError:
    print("\nErro: Por favor, digite um número válido (ex: 10 ou 2.5).")