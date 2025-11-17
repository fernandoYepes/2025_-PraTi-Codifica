"""
4. Crie um programa que leia o tamanho de três segmentos de reta. Analise seus
comprimentos e diga se é possível formar um triângulo com essas retas.
Matematicamente, para três segmentos formarem um triângulo, o comprimento de cada
lado deve ser menor que a soma dos outros dois.
"""

print("--- Analisador de Formação de Triângulos ---")
print("Digite o comprimento dos três segmentos:")

# Bloco try-except para garantir que o usuário digite números
try:
    r1 = float(input("Comprimento do Segmento 1: "))
    r2 = float(input("Comprimento do Segmento 2: "))
    r3 = float(input("Comprimento do Segmento 3: "))

    # Verificar se os comprimentos são válidos (maiores que zero)
    if r1 <= 0 or r2 <= 0 or r3 <= 0:
        print("\nErro: Os comprimentos dos segmentos devem ser números positivos.")
    else:
        # O 'and' garante que TODAS as três condições sejam verdadeiras.
        
        condicao1 = r1 < (r2 + r3)
        condicao2 = r2 < (r1 + r3)
        condicao3 = r3 < (r1 + r2)

        pode_formar = condicao1 and condicao2 and condicao3

        if pode_formar:
            
            print(f"\nCom os segmentos {r1}, {r2} e {r3}, É POSSÍVEL formar um triângulo.")
        else:
            print(f"\nCom os segmentos {r1}, {r2} e {r3}, NÃO É POSSÍVEL formar um triângulo.")
            # Opcional: explicar por que falhou
            if not condicao1:
                print(f"Motivo: O segmento {r1} é maior ou igual à soma dos outros dois ({r2+r3}).")
            elif not condicao2:
                print(f"Motivo: O segmento {r2} é maior ou igual à soma dos outros dois ({r1+r3}).")
            elif not condicao3:
                print(f"Motivo: O segmento {r3} é maior ou igual à soma dos outros dois ({r1+r2}).")

except ValueError:
    print("\nErro: Por favor, digite um número válido (ex: 10 ou 7.5).")