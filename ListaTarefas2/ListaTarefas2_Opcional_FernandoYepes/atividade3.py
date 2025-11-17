"""
3. Faça um algoritmo que pergunte a distância que um passageiro deseja percorrer em
Km. Calcule o preço da passagem, cobrando R$ 0.50 por Km para viagens até 200 Km e
R$ 0.45 para viagens mais longas.
"""

# --- Constantes de Preço ---
LIMITE_DISTANCIA = 200  # A distância onde o preço muda
PRECO_CURTO = 0.50      # Preço para viagens até 200 Km
PRECO_LONGO = 0.45      # Preço para viagens acima de 200 Km

print("--- Calculadora de Preço de Passagem ---")

try:
    # Usa float() porque a distância pode ser "quebrada" (ex: 150.5 Km)
    distancia = float(input("Qual a distância da sua viagem (em Km)? "))

    # verificação para evitar números negativos
    if distancia < 0:
        print("Erro: A distância não pode ser um número negativo.")
    else:
    
        if distancia <= LIMITE_DISTANCIA:
            # Viagem curta (200 Km ou menos)
            preco = distancia * PRECO_CURTO
            tarifa_usada = PRECO_CURTO
        else:
            # Viagem longa (mais de 200 Km)
            preco = distancia * PRECO_LONGO
            tarifa_usada = PRECO_LONGO

        print("\n--- Resumo da Viagem ---")
        print(f"Distância a percorrer: {distancia} Km")
        print(f"Tarifa aplicada: R$ {tarifa_usada:.2f} por Km")
        # Usa :.2f para formatar o preço em Reais (duas casas decimais)
        print(f"Preço total da passagem: R$ {preco:.2f}")
        print("-------------------------")

except ValueError:
    print("\nErro: Por favor, digite um número válido (ex: 150 ou 300.5).")