"""
22. A prefeitura de uma cidade fez uma pesquisa entre os seus habitantes, coletando
dados sobre o salário e número de filhos. Faça uma função que leia esses dados para um
número não determinado de pessoas e retorne a média de salário da população, a

média do número de filhos, o maior salário e o percentual de pessoas com salário até R$
350,00.
"""

def coletar_dados_pesquisa():
    
    total_pessoas = 0
    soma_salario = 0.0
    soma_filhos = 0
    maior_salario = 0.0
    contador_salario_baixo = 0
    SALARIO_LIMITE = 350.00
    
    print("--- Pesquisa da Prefeitura ---")
    print("Digite os dados dos habitantes. (Pressione 'N' para parar)")

    while True:
        print(f"\n--- Habitante {total_pessoas + 1} ---")
        
        while True:
            try:
                salario = float(input("Digite o salário: R$ "))
                if salario < 0:
                    print("Erro: O salário não pode ser negativo. Tente novamente.")
                else:
                    break
            except ValueError:
                print("Erro: Digite um valor numérico (ex: 1500.50).")

        while True:
            try:
                filhos = int(input("Digite o número de filhos: "))
                if filhos < 0:
                    print("Erro: O número de filhos não pode ser negativo.")
                else:
                    break
            except ValueError:
                print("Erro: Digite um número inteiro (ex: 2).")

        total_pessoas += 1
        soma_salario += salario
        soma_filhos += filhos
        
        if salario > maior_salario:
            maior_salario = salario
            
        if salario <= SALARIO_LIMITE:
            contador_salario_baixo += 1
            
        while True:
            continuar = input("\nDeseja registrar outro habitante? [S/N]: ").lower().strip()
            if continuar == 's' or continuar == 'n':
                break
            else:
                print("Erro: Resposta inválida. Digite 'S' ou 'N'.")
                
        if continuar == 'n':
            break

    if total_pessoas == 0:
        print("Nenhum dado foi inserido.")
        return 0.0, 0.0, 0.0, 0.0, 0
        
    media_salario = soma_salario / total_pessoas
    media_filhos = soma_filhos / total_pessoas
    perc_salario_baixo = (contador_salario_baixo / total_pessoas) * 100
    
    return media_salario, media_filhos, maior_salario, perc_salario_baixo, total_pessoas


# --- Programa Principal ---
print("Iniciando a coleta de dados da pesquisa...")

media_s, media_f, maior_s, perc_baixo, total_p = coletar_dados_pesquisa()

print("\n" + "=" * 30)
print("--- RESULTADO DA PESQUISA ---")
print("=" * 30)

if total_p > 0:
    print(f"Total de Pessoas: {total_p}")
    print(f"Média de Salário da População: R$ {media_s:.2f}")
    print(f"Média do Número de Filhos: {media_f:.1f}")
    print(f"Maior Salário Encontrado: R$ {maior_s:.2f}")
    print(f"Percentual (Salário <= R$ 350,00): {perc_baixo:.1f}%")
else:
    print("Nenhum habitante foi registrado.")