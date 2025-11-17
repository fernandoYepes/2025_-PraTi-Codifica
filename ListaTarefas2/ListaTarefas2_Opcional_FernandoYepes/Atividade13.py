"""
13. Crie um programa que preencha automaticamente (usando lógica, não apenas
atribuindo diretamente) um vetor numérico com 15 posições com os primeiros elementos
da sequência de Fibonacci.
"""

print("--- Vetor com 15 Termos de Fibonacci ---")

vetor_fibonacci = []

a = 0
b = 1

for i in range(15):
    
    vetor_fibonacci.append(b)
    
    proximo_termo = a + b
    
    a = b
    b = proximo_termo

print("\nVetor preenchido:")
print(vetor_fibonacci)

print(f"\nO vetor tem {len(vetor_fibonacci)} elementos.")