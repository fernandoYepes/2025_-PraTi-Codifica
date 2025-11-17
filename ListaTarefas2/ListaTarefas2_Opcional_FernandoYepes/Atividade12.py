"""
Faça um programa que mostre os 10 primeiros elementos da Sequência de Fibonacci.
Ex.: 1, 1, 2, 3, 5, 8, 13, 21.
"""
print("--- 10 Primeiros Termos de Fibonacci ---")

termo_1 = 1
termo_2 = 1

print(f"{termo_1}", end=" -> ")
print(f"{termo_2}", end=" -> ")

for i in range(8):
    termo_3 = termo_1 + termo_2
    print(f"{termo_3}", end=" -> ")
    
    termo_1 = termo_2
    termo_2 = termo_3

print("FIM")