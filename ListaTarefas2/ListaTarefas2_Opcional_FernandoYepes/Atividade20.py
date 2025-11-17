"""
20. Uma indústria faz a folha mensal de pagamentos de seus 80 empregados baseada
no seguinte: existe uma tabela com os dados de cada funcionalidade: matrícula, nome e
salário bruto. Escreva um programa que leia e processe a tabela e emita (escreva na
tela), cada funcionário, seu contracheque, cujo formato é dado a seguir:
Matrícula:
Nome:
Salário bruto:
Dedução INSS:
Salário líquido:
(Dicas: desconto de 12%, salário líquido é a diferença entre salário bruto e a redução do
INSS).
"""

print("--- Processamento da Folha de Pagamento ---")

TAXA_INSS = 0.12  # 12% de dedução
contador = 0

while True:
    contador += 1
    print(f"\n--- Lendo Dados do Funcionário {contador} ---")

    matricula = input("Matrícula do funcionário: ").strip()
    nome = input("Nome do funcionário: ").strip()

    while True:
        try:
            salario_bruto_str = input(f"Salário Bruto de {nome}: R$ ")
            salario_bruto = float(salario_bruto_str)
            
            if salario_bruto < 0:
                print("Erro: O salário não pode ser um número negativo.")
            else:
                break
        except ValueError:
            print("Erro: Por favor, digite um valor numérico (ex: 3500.50).")

    deducao_inss = salario_bruto * TAXA_INSS
    salario_liquido = salario_bruto - deducao_inss

    print("\n" + ("-" * 30))
    print("--- [ CONTRACHEQUE ] ---")
    print(f"Matrícula: \t{matricula}")
    print(f"Nome: \t\t{nome}")
    print("-" * 30)
    print(f"Salário Bruto: \tR$ {salario_bruto:.2f}")
    print(f"Dedução INSS (12%): \tR$ {deducao_inss:.2f}")
    print(f"Salário Líquido: \tR$ {salario_liquido:.2f}")
    print("=" * 30)

    while True:
        continuar = input("\nDeseja registrar outro funcionário? [S/N]: ").lower().strip()
        if continuar == 's' or continuar == 'n':
            break
        else:
            print("Erro: Resposta inválida. Por favor, digite 'S' ou 'N'.")
            
    if continuar == 'n':
        break

print(f"\nProcessamento finalizado. {contador} funcionários registrados.")