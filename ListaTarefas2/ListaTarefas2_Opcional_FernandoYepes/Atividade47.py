"""
47. Crie uma função que transforme um objeto de entrada aplicando uma função
fornecida a cada uma das propriedades do objeto, retornando um novo objeto com os
resultados.
"""

def transformar_objeto(objeto_entrada, funcao_transformadora):

    return {chave: funcao_transformadora(valor) for chave, valor in objeto_entrada.items()}


def dobrar_valor(valor):

    if isinstance(valor, (int, float)):
        return valor * 2
    return valor

def colocar_em_maiusculo(valor):

    if isinstance(valor, str):
        return valor.upper()
    return valor



print("--- Transformador de Objeto (Dicionário) ---")

objeto_original = {
    'item': 'Produto A',
    'quantidade': 10,
    'preco': 15.50,
    'ativo': True
}

print("\n--- Objeto Original ---")
print(objeto_original)

objeto_transformado_1 = transformar_objeto(objeto_original, dobrar_valor)

print("\n" + "=" * 40)
print("--- Objeto Transformado (Dobrando números) ---")
print("=" * 40)
print(objeto_transformado_1)

objeto_transformado_2 = transformar_objeto(objeto_original, colocar_em_maiusculo)

print("\n" + "=" * 40)
print("--- Objeto Transformado (Strings em maiúsculo) ---")
print("=" * 40)
print(objeto_transformado_2)