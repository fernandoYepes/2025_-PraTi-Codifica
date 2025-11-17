"""
49. Você recebe um array de objetos representando transações financeiras. Cada
transação possui id, valor, data, e categoria. Escreva uma função que retorne um objeto
onde as chaves são as categorias, e os valores são arrays de transações pertencentes a
essa categoria. Adicionalmente, inclua um subtotal de valores por categoria.
"""

from collections import defaultdict
import json

def agrupar_por_categoria(transacoes):

    
    grupos = defaultdict(lambda: {
        'transacoes': [],
        'subtotal': 0.0
    })
    
    for transacao in transacoes:
        categoria = transacao['categoria']
        valor = transacao['valor']
        
        grupos[categoria]['transacoes'].append(transacao)
        grupos[categoria]['subtotal'] += valor
        
    return dict(grupos)



print("--- Agrupador de Transações Financeiras ---")

array_transacoes = [
    {'id': 1, 'valor': 50.00, 'data': '2025-10-01', 'categoria': 'Alimentação'},
    {'id': 2, 'valor': 80.00, 'data': '2025-10-01', 'categoria': 'Transporte'},
    {'id': 3, 'valor': 120.00, 'data': '2025-10-02', 'categoria': 'Alimentação'},
    {'id': 4, 'valor': 200.00, 'data': '2025-10-03', 'categoria': 'Lazer'},
    {'id': 5, 'valor': 35.00, 'data': '2025-10-03', 'categoria': 'Transporte'},
    {'id': 6, 'valor': 150.00, 'data': '2025-10-04', 'categoria': 'Lazer'},
]

print("\n--- Array Original de Transações ---")
print(json.dumps(array_transacoes, indent=2, ensure_ascii=False))

transacoes_agrupadas = agrupar_por_categoria(array_transacoes)

print("\n" + "=" * 40)
print("--- Objeto Agrupado por Categoria (com Subtotais) ---")
print("=" * 40)
print(json.dumps(transacoes_agrupadas, indent=2, ensure_ascii=False))