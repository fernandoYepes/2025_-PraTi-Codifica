# -*- coding: utf-8 -*-

"""
7. Uma empresa de aluguel de carros precisa cobrar pelos seus serviços. O aluguel de um
carro popular custa R$ 90,00 por dia e um carro de luxo custa R$ 150,00. Além disso, o
cliente paga por Km percorrido. Faça um programa que leia o tipo de carro alugado
(popular ou luxo), quantos dias de aluguel e quantos Km foram percorridos. No final,
mostre o preço a ser pago de acordo com os dados a seguir:
Carros populares
- Até 100 Km percorridos: R$ 0,20 por Km
- Acima de 100 Km percorridos: R$ 0,10 por Km
Carros de luxo
- Até 200 Km percorridos: R$ 0,30 por Km
- Acima de 200 Km percorridos: R$ 0,25 por Km
"""

# Tarifas Diárias
PRECO_DIA_POPULAR = 90.00
PRECO_DIA_LUXO = 150.00

# Tarifas de Km - Popular
LIMITE_KM_POPULAR = 100
PRECO_KM_POPULAR_CURTO = 0.20  # Até 100 Km
PRECO_KM_POPULAR_LONGO = 0.10  # Acima de 100 Km

# Tarifas de Km - Luxo
LIMITE_KM_LUXO = 200
PRECO_KM_LUXO_CURTO = 0.30  # Até 200 Km
PRECO_KM_LUXO_LONGO = 0.25  # Acima de 200 Km

print("--- Calculadora de Aluguel de Carros ---")


try:
    
    # Usa .lower().strip() para limpar a entrada (remove espaços e converte para minúscula)
    tipo_carro = input("Qual o tipo de carro? [P]opular ou [L]uxo: ").lower().strip()
    
    dias = int(input("Quantos dias de aluguel? "))
    km = float(input("Quantos Km foram percorridos? "))

    # Valida se números são positivos
    if dias <= 0 or km < 0:
        print("\nErro: O número de dias deve ser ao menos 1 e a Km não pode ser negativa.")

    #  CARRO POPULAR
    elif tipo_carro == 'p' or tipo_carro == 'popular':
        
        custo_diaria = dias * PRECO_DIA_POPULAR
        
        # Custo variável por Km
        if km <= LIMITE_KM_POPULAR:
            custo_km = km * PRECO_KM_POPULAR_CURTO
            tarifa_km_usada = PRECO_KM_POPULAR_CURTO
        else:
            custo_km = km * PRECO_KM_POPULAR_LONGO
            tarifa_km_usada = PRECO_KM_POPULAR_LONGO
            
        # Total
        total = custo_diaria + custo_km
        
        print("\n--- Resumo: Carro POPULAR ---")
        print(f"Custo por {dias} dias: R$ {custo_diaria:.2f}")
        print(f"Custo por {km} Km (tarifa R$ {tarifa_km_usada:.2f}/Km): R$ {custo_km:.2f}")
        print("-" * 30)
        print(f"TOTAL A PAGAR: R$ {total:.2f}")

    # CARRO DE LUXO
    elif tipo_carro == 'l' or tipo_carro == 'luxo':

        custo_diaria = dias * PRECO_DIA_LUXO
        
        # Custo variável por Km
        if km <= LIMITE_KM_LUXO:
            custo_km = km * PRECO_KM_LUXO_CURTO
            tarifa_km_usada = PRECO_KM_LUXO_CURTO
        else:
            custo_km = km * PRECO_KM_LUXO_LONGO
            tarifa_km_usada = PRECO_KM_LUXO_LONGO
            
        # total
        total = custo_diaria + custo_km
        
        print("\n--- Resumo: Carro de LUXO ---")
        print(f"Custo por {dias} dias: R$ {custo_diaria:.2f}")
        print(f"Custo por {km} Km (tarifa R$ {tarifa_km_usada:.2f}/Km): R$ {custo_km:.2f}")
        print("-" * 30)
        print(f"TOTAL A PAGAR: R$ {total:.2f}")

    # Erro
    else:
        print(f"\nErro: Tipo de carro '{tipo_carro}' não reconhecido.")
        print("Por favor, digite 'P' (ou 'popular') ou 'L' (ou 'luxo').")

except ValueError:
    print("\nErro: Por favor, digite um NÚMERO válido para os dias e Km.")
except Exception as e:
    print(f"\nOcorreu um erro inesperado: {e}")