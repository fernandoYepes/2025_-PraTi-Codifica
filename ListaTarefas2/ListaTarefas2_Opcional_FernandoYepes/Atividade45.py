"""
45. Dado um array de strings, crie um objeto onde cada string é uma chave, e seu valor é
o número de vezes que a string aparece no array.
"""

print("--- Contador de Frequência de Strings ---")

array_strings = [
    'maçã', 'banana', 'laranja', 'maçã', 'uva',
    'banana', 'maçã', 'abacate', 'laranja', 'banana'
]

print("\n--- Array Original ---")
print(array_strings)

objeto_contagem = {}

for string in array_strings:
    if string in objeto_contagem:
        objeto_contagem[string] += 1
    else:
        objeto_contagem[string] = 1

print("\n" + "=" * 40)
print("--- Objeto de Contagem (Frequência) ---")
print("=" * 40)
print(objeto_contagem)