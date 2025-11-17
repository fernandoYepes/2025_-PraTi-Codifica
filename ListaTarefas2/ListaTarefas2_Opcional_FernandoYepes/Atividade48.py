"""
48. Você recebe dois objetos que representam o inventário de duas lojas diferentes:
inventarioLojaA e inventarioLojaB. Cada chave é um item, e o valor é a quantidade desse
item em estoque. Escreva uma função que combine os inventários em um único objeto.
Se um item aparecer em ambas as lojas, some as quantidades.
"""

def combinar_inventarios(inventario_a, inventario_b):

    
    inventario_total = inventario_a.copy()
    
    for item, quantidade_b in inventario_b.items():
        if item in inventario_total:
            inventario_total[item] += quantidade_b
        else:
            inventario_total[item] = quantidade_b
            
    return inventario_total


print("--- Combinador de Inventários de Lojas ---")

inventarioLojaA = {
    'maçã': 10,
    'banana': 20,
    'laranja': 15
}

inventarioLojaB = {
    'banana': 30,
    'uva': 25,
    'maçã': 5
}

print("\n--- Inventário Loja A ---")
print(inventarioLojaA)

print("\n--- Inventário Loja B ---")
print(inventarioLojaB)

inventario_combinado = combinar_inventarios(inventarioLojaA, inventarioLojaB)

print("\n" + "=" * 40)
print("--- Inventário Total Combinado ---")
print("=" * 40)
print(inventario_combinado)