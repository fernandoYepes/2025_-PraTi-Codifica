"""
10. Crie um programa usando a estrutura “faça enquanto” que leia vários números. A
cada laço, pergunte se o usuário quer continuar ou não. No final, mostre na tela:
a) O somatório entre todos os valores;
b) Qual foi o menor valor digitado;
c) A média entre todos os valores;
d) Quantos valores são pares.
"""

print("--- Analisador de Números ---")
print("Digite quantos valores desejar. (Pressione 'N' para parar)")

contador = 0
soma = 0.0
menor_valor = None 
valores_pares = 0

# Loop "Faça-Enquanto" (do-while)
while True:
    
    # Validar a entrada do número
    while True:
        try:
            # Usa float para aceitar números decimais
            num = float(input(f"\nDigite o {contador + 1}º valor: "))
            break # Sai do loop de validação se o número for válido
        except ValueError:
            print("Erro: Por favor, digite um valor numérico (ex: 10 ou 7.5).")

    soma += num
    
    if menor_valor is None or num < menor_valor:
        menor_valor = num
        
    contador += 1
    
    if num % 2 == 0:
        valores_pares += 1
        
    
    # Pergunta se o usuário quer continuar
    while True:
        continuar = input("Deseja continuar? [S/N]: ").lower().strip()
        if continuar == 's' or continuar == 'n':
            break # Sai do loop de validação se a resposta for 's' ou 'n'
        else:
            print("Erro: Resposta inválida. Por favor, digite 'S' para Sim ou 'N' para Não.")
            
    if continuar == 'n':
        break # Este 'break' encerra o 'while True' principal

# Exibir o relatório final
media = soma / contador

print("\n" + "=" * 30)
print("--- RELATÓRIO FINAL ---")
print("=" * 30)
print(f"Total de valores digitados: {contador}")
print(f"a) O somatório total foi: R$ {soma:.2f}")
print(f"b) O menor valor digitado foi: R$ {menor_valor:.2f}")
print(f"c) A média entre os valores foi: R$ {media:.2f}")
print(f"d) Quantidade de valores pares: {valores_pares}")
print("=" * 30)