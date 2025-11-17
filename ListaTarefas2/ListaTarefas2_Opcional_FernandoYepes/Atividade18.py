"""
18. Crie um registro com o nome do funcionário, cargo e salário. Leia este registro para
um funcionário e ao final escreva o conteúdo do registro.
"""

print("--- Cadastro de Funcionário (Registro Único) ---")

funcionario = {}

print("Por favor, preencha os dados do funcionário:")

funcionario['nome'] = input("Nome do funcionário: ").strip()
funcionario['cargo'] = input("Cargo do funcionário: ").strip()

while True:
    try:
        salario_str = input(f"Salário de {funcionario['nome']}: R$ ")
        salario_float = float(salario_str)
        
        if salario_float < 0:
            print("Erro: O salário não pode ser um número negativo. Tente novamente.")
        else:
            funcionario['salario'] = salario_float
            break
            
    except ValueError:
        print("Erro: Por favor, digite um valor numérico para o salário (ex: 3500.50).")

print("\n" + "=" * 30)
print("--- Dados do Funcionário Registrado ---")
print("=" * 30)

print(f"Nome: \t\t{funcionario['nome']}")
print(f"Cargo: \t\t{funcionario['cargo']}")
print(f"Salário: \tR$ {funcionario['salario']:.2f}")