"""
2. Escreva um programa que pergunte a velocidade de um carro. Caso ultrapasse 80 Km
h-1, exiba uma mensagem dizendo que o usuário foi multado. Nesse caso, exiba o valor da
multa, cobrando R$ 5,00 por cada Km acima da velocidade permitida.
"""

LIMITE_VELOCIDADE = 80
VALOR_POR_KM = 5.00

print("--- Fiscalização de Velocidade ---")

# Bloco try-except para garantir que o usuário digite um número
try:
    velocidade = int(input("Qual a velocidade do carro (em Km/h)? "))

    if velocidade > LIMITE_VELOCIDADE:
        # Se a velocidade for maior que 80...
    
        km_acima = velocidade - LIMITE_VELOCIDADE
        
        multa = km_acima * VALOR_POR_KM
        
        print("\n--- MULTADO! ---")
        print(f"Você ultrapassou o limite de {LIMITE_VELOCIDADE} Km/h.")
        print(f"Você estava a {km_acima} Km/h acima do permitido.")
        # Usamos :.2f para formatar o dinheiro (ex: 75.00)
        print(f"Valor da multa: R$ {multa:.2f}")
        print("------------------")

    else:
        # Se a velocidade for 80 ou menos...
        print(f"\nVelocidade permitida ({velocidade} Km/h).")
        print("Tenha um bom dia e dirija com segurança!")

except ValueError:
    print("\nErro: Por favor, digite apenas um número (como 90 ou 75).")