"""
17. Crie um programa que leia o nome e a idade de 9 pessoas e guarde esses valores em
dois vetores, em posições relacionadas. No final, mostre uma listagem contendo apenas
os dados das pessoas menores de idade.
"""

print("--- Cadastro de Pessoas (Filtro de Menores) ---")

vetor_nomes = []
vetor_idades = []
TOTAL_PESSOAS = 9
IDADE_MAIORIDADE = 18

print(f"Por favor, digite o nome e a idade de {TOTAL_PESSOAS} pessoas.")

for i in range(TOTAL_PESSOAS):
    print(f"\n--- Pessoa {i + 1} de {TOTAL_PESSOAS} ---")
    
    nome = input(f"Nome da {i + 1}ª pessoa: ").strip()
    
    while True:
        try:
            idade_str = input(f"Idade de {nome}: ")
            idade_int = int(idade_str)
            
            if idade_int < 0:
                print("Erro: A idade não pode ser um número negativo. Tente novamente.")
            else:
                vetor_nomes.append(nome)
                vetor_idades.append(idade_int)
                break
        except ValueError:
            print("Erro: Por favor, digite um NÚMERO INTEIRO para a idade (ex: 15).")

print("\n" + "=" * 30)
print(f"--- Listagem: Menores de {IDADE_MAIORIDADE} anos ---")
print("=" * 30)

encontrou_menor = False

for i in range(TOTAL_PESSOAS):
    
    if vetor_idades[i] < IDADE_MAIORIDADE:
        print(f"Nome: {vetor_nomes[i]} \t- Idade: {vetor_idades[i]} anos")
        encontrou_menor = True

if not encontrou_menor:
    print("Nenhuma pessoa menor de idade foi cadastrada.")