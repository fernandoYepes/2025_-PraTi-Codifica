"""
44. Escreva uma função que conte quantas propriedades do tipo string existem em um
objeto e retorne esse número.
"""

def contar_strings(objeto):

    contador = 0
    for valor in objeto.values():
        if isinstance(valor, str):
            contador += 1
    return contador


print("--- Contador de Propriedades String ---")

dados_teste = {
    'id': 123,
    'nome': 'Projeto A',
    'concluido': False,
    'tags': ['python', 'dev', 'filtro'],
    'descricao': 'Um projeto de teste.',
    'membros': [7, 12, 15],
    'status': 'Ativo'
}

print("\n--- Objeto de Teste ---")
print(dados_teste)

numero_de_strings = contar_strings(dados_teste)

print("\n" + "=" * 40)
print("--- Resultado ---")
print("=" * 40)
print(f"O objeto contém {numero_de_strings} propriedades do tipo string.")