"""
8. Um programa de vida saudável quer dar pontos por atividades físicas realizadas que
podem ser trocados por dinheiro. Cada hora de atividade física no mês vale pontos. O
sistema funciona assim:
- até 10 h de atividade no mês: ganha 2 pontos por hora
- de 10 h até 20 h de atividade no mês: ganha 5 pontos por hora
- acima de 20 h de atividade no mês: ganha 10 pontos por hora
- A cada ponto ganho, o cliente fatura R$ 0,05 (5 centavos)
Faça um programa que leia quantas horas de atividade uma pessoa teve por mês.
Calcule e mostre quantos pontos ela teve e quanto dinheiro ela conseguiu ganhar.
"""

VALOR_POR_PONTO = 0.05

# Limites de horas
LIMITE_NIVEL_1 = 10
LIMITE_NIVEL_2 = 20

# Multiplicadores de pontos
PONTOS_NIVEL_1 = 2
PONTOS_NIVEL_2 = 5
PONTOS_NIVEL_3 = 10

print("--- Calculadora de Pontos de Atividade ---")

# Bloco try-except para garantir que o usuário digite um número
try:
    horas = float(input("Quantas horas de atividade você teve no mês? "))

    # 2. Valida se a hora é um número positivo
    if horas < 0:
        print("\nErro: O número de horas não pode ser negativo.")
    else:
        # Lógica para definir a taxa de pontos
        
        if horas <= LIMITE_NIVEL_1:
            # Até 10 horas
            pontos_por_hora = PONTOS_NIVEL_1
            
        elif horas <= LIMITE_NIVEL_2:
            # Entre 10.01 e 20 horas
            pontos_por_hora = PONTOS_NIVEL_2
            
        else:
            # Acima de 20 horas
            pontos_por_hora = PONTOS_NIVEL_3
            
        total_pontos = horas * pontos_por_hora
        total_dinheiro = total_pontos * VALOR_POR_PONTO
        
        print("\n--- Resumo do Mês ---")
        print(f"Horas de atividade: {horas} h")
        print(f"Tarifa aplicada: {pontos_por_hora} pontos por hora")
        print(f"Total de pontos ganhos: {total_pontos:.1f} pontos")
        print("-" * 30)
        print(f"Dinheiro faturado: R$ {total_dinheiro:.2f}")

except ValueError:
    print("\nErro: Por favor, digite um número válido (ex: 12 ou 15.5).")