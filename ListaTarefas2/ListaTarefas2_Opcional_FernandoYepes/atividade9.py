"""
9. Desenvolva um aplicativo que leia o salário e o sexo de vários funcionários. No final,
mostre o total de salário pago aos homens e o total pago às mulheres. O programa vai
perguntar ao usuário se ele quer continuar ou não sempre que ler os dados de um
funcionário.
"""

print("--- Controle de Pagamentos por Sexo ---")

total_salario_homens = 0.0
total_salario_mulheres = 0.0
contador_homens = 0
contador_mulheres = 0

# laço infinito que será quebrado pelo usuário
while True:
    print(f"\n--- Cadastro do Funcionário {contador_homens + contador_mulheres + 1} ---")
    
    # Valida a entrada do Salário
    while True:
        try:
            salario = float(input("Digite o salário: R$ "))
            if salario < 0:
                print("Erro: O salário não pode ser um valor negativo. Tente novamente.")
            else:
                break
        except ValueError:
            print("Erro: Por favor, digite um valor numérico (ex: 2500.50).")

    # Valida a entrada do Sexo
    while True:
        sexo = input("Digite o sexo [M/F]: ").lower().strip()
        if sexo == 'm' or sexo == 'f':
            break # Sai do loop de sexo se a entrada for 'm' ou 'f'
        else:
            print("Erro: Resposta inválida. Por favor, digite 'M' para Masculino ou 'F' para Feminino.")
    
    # cumular os valores
    if sexo == 'm':
        total_salario_homens += salario
        contador_homens += 1
    elif sexo == 'f':
        total_salario_mulheres += salario
        contador_mulheres += 1
        
    while True:
        continuar = input("\nDeseja cadastrar outro funcionário? [S/N]: ").lower().strip()
        if continuar == 's' or continuar == 'n':
            break # Sai do loop de "continuar" se a resposta for 's' ou 'n'
        else:
            print("Erro: Resposta inválida. Por favor, digite 'S' para Sim ou 'N' para Não.")
            
    if continuar == 'n':
        print("\nEncerrando o cadastro...")
        break # Este 'break' encerra o 'while True' principal
4
print("=" * 40)
print("--- RELATÓRIO FINAL DE PAGAMENTOS ---")
print("=" * 40)

print("\n--- HOMENS ---")
print(f"Total de funcionários: {contador_homens}")
print(f"Total de salários pagos: R$ {total_salario_homens:.2f}")

print("\n--- MULHERES ---")
print(f"Total de funcionárias: {contador_mulheres}")
print(f"Total de salários pagos: R$ {total_salario_mulheres:.2f}")

print("\n" + "=" * 40)