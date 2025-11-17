"""
42. Crie um objeto chamado dados que contém várias propriedades, incluindo números,
strings e arrays. Escreva uma função que retorne um novo objeto apenas com as
propriedades que são arrays.
"""

def filtrar_arrays(dados_originais):

    dados_filtrados = {}
    
    for chave, valor in dados_originais.items():
        if isinstance(valor, list):
            dados_filtrados[chave] = valor
            
    return dados_filtrados



print("--- Filtro de Propriedades (Arrays) ---")

dados = {
    'id': 123,
    'nome': 'Projeto A',
    'concluido': False,
    'tags': ['python', 'dev', 'filtro'],
    'membros': [7, 12, 15],
    'orcamento': 1500.50,
    'departamentos': ['Engenharia', 'QA']
}

print("\n--- Objeto Original (Dicionário) ---")
print(dados)

arrays_encontrados = filtrar_arrays(dados)

print("\n" + "=" * 40)
print("--- Novo Objeto (Apenas propriedades que são Arrays) ---")
print("=" * 40)
print(arrays_encontrados)