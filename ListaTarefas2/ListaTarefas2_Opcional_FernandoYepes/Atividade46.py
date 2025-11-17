"""
46. Suponha que você tem um array de objetos onde cada objeto representa uma venda
com vendedor e valor. Escreva uma função que retorne um objeto que sumarize o total
de vendas por vendedor.
"""

def sumarizar_vendas(array_de_vendas):

    sumario = {}
    
    for venda in array_de_vendas:
        vendedor = venda['vendedor']
        valor = venda['valor']
        
        if vendedor in sumario:
            sumario[vendedor] += valor
        else:
            sumario[vendedor] = valor
            
    return sumario


print("--- Sumarizador de Vendas por Vendedor ---")

array_vendas = [
    {'vendedor': 'Ana', 'valor': 100},
    {'vendedor': 'Bruno', 'valor': 150},
    {'vendedor': 'Ana', 'valor': 200},
    {'vendedor': 'Carla', 'valor': 50},
    {'vendedor': 'Bruno', 'valor': 300},
    {'vendedor': 'Ana', 'valor': 120},
    {'vendedor': 'Carla', 'valor': 250},
]

print("\n--- Array Original de Vendas ---")
print(array_vendas)

sumario_total = sumarizar_vendas(array_vendas)

print("\n" + "=" * 40)
print("--- Objeto (Sumário) Total por Vendedor ---")
print("=" * 40)
print(sumario_total)