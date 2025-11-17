"""
43. Dado dois objetos, obj1 e obj2, escreva uma função que crie um novo objeto
combinando as propriedades de ambos, onde as propriedades de obj2 têm precedência
sobre as do obj1 em caso de conflitos.
"""

def combinar_objetos(obj1, obj2):

    
    novo_obj = {**obj1, **obj2}
    return novo_obj


print("--- Combinador de Objetos (Dicionários) ---")

obj1 = {
    'nome': 'Ana',
    'idade': 30,
    'cidade': 'São Paulo'
}

obj2 = {
    'idade': 31,
    'cidade': 'Rio de Janeiro',
    'email': 'ana@exemplo.com'
}

print("\n--- Objeto 1 ---")
print(obj1)

print("\n--- Objeto 2 (Tem precedência) ---")
print(obj2)

objeto_combinado = combinar_objetos(obj1, obj2)

print("\n" + "=" * 40)
print("--- Objeto Combinado (obj2 sobrepôs obj1) ---")
print("=" * 40)
print(objeto_combinado)