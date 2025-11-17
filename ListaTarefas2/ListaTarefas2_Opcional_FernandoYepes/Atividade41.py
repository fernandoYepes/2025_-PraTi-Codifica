"""
41. Dado o objeto pessoa com propriedades nome e idade, acesse e imprima o valor de
idade. Adicione uma nova propriedade chamada email ao objeto pessoa que já possui
nome e idade.
"""

print("--- Manipulação de Objeto (Dicionário) ---")

pessoa = {
    'nome': 'Ana Silva',
    'idade': 30
}

print("\n--- Objeto Original ---")
print(pessoa)

print("\n" + "=" * 30)
print("1. Acessando e imprimindo a idade:")
idade_da_pessoa = pessoa['idade']
print(f"A idade é: {idade_da_pessoa}")

print("\n" + "=" * 30)
print("2. Adicionando a propriedade 'email'...")
pessoa['email'] = 'ana.silva@exemplo.com'

print("\n--- Objeto Modificado (com email) ---")
print(pessoa)