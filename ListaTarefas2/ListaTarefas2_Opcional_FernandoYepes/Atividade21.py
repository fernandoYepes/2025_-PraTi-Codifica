"""
21. Faça uma função que recebe, por parâmetro, a altura (alt) e o sexo de uma pessoa e
retorna o seu peso ideal. Para homens, calcular o peso ideal usando a fórmula: peso ideal
= 72.7 x alt - 58 e, para mulheres, peso ideal = 62.1 x alt - 44.7.
"""

def calcular_peso_ideal(alt, sexo):
    ##Retorna o peso ideal (float) or None se o sexo for inválido.
    sexo_limpo = sexo.lower().strip()
    
    if sexo_limpo == 'm' or sexo_limpo == 'masculino':
        peso_ideal = (72.7 * alt) - 58
        return peso_ideal
    elif sexo_limpo == 'f' or sexo_limpo == 'feminino':
        peso_ideal = (62.1 * alt) - 44.7
        return peso_ideal
    else:
        return None

print("--- Calculadora de Peso Ideal ---")

while True:
    try:
        altura_input = float(input("Digite a altura (ex: 1.75): "))
        if altura_input <= 0:
            print("Erro: A altura deve ser um número positivo.")
        else:
            break
    except ValueError:
        print("Erro: Digite um valor numérico para a altura (use '.' como decimal).")

while True:
    sexo_input = input("Digite o sexo [M/F]: ").strip()
    if sexo_input.lower() in ['m', 'f', 'masculino', 'feminino']:
        break
    else:
        print("Erro: Resposta inválida. Digite 'M' para Masculino ou 'F' para Feminino.")

peso_calculado = calcular_peso_ideal(altura_input, sexo_input)

if peso_calculado is not None:
    print("\n" + "=" * 30)
    print("--- Resultado ---")
    print(f"Altura: {altura_input}m")
    print(f"Sexo: {sexo_input.upper()}")
    print(f"Peso Ideal: {peso_calculado:.2f} Kg")
    print("=" * 30)
else:
    print("Ocorreu um erro inesperado no cálculo (sexo inválido).")