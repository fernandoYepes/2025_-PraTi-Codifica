"""
Escreva um programa para calcular a redução do tempo de vida de um fumante.
Pergunte a quantidade de cigarros fumados por dias e quantos anos ele já fumou.
Considere que um fumante perde 10 min de vida a cada cigarro. Calcule quantos dias de
vida um fumante perderá e exiba o total em dias.
"""

print("--- Calculadora de Tempo de Vida (Fumante) ---")

# Bloco try-except para garantir que o usuário digite apenas números
try:
    cigarros_por_dia = int(input("Quantos cigarros você fuma por dia? "))
    anos_fumados = int(input("Você fuma há quantos anos? "))


    #  Calcular o total de cigarros fumados na vida
    total_dias_fumando = anos_fumados * 365
    total_cigarros = total_dias_fumando * cigarros_por_dia

    #  Calcular o total de minutos perdidos
    minutos_perdidos = total_cigarros * 10

    #  Converter o total de minutos para dias
    minutos_por_dia = 24 * 60
    dias_perdidos = minutos_perdidos / minutos_por_dia

    print("\n--- Resultado ---")
    print(f"Ao fumar {cigarros_por_dia} cigarros por dia durante {anos_fumados} anos,")
    print(f"você já perdeu aproximadamente {round(dias_perdidos)} dias de vida.")
    print("-------------------")

except ValueError:
    print("\nErro: Por favor, digite apenas números inteiros (como 10 ou 5).")