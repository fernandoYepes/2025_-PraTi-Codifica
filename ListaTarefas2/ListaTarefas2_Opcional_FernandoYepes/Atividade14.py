"""
14. Faça um programa que leia 7 nomes de pessoas e guarde-os em um vetor. No final,
mostre uma listagem com todos os nomes informados, na ordem inversa daquela em
que eles foram informados.
"""

print("--- Listador de Nomes Inversos ---")

vetor_nomes = []

print("Por favor, digite 7 nomes:")

for i in range(7):
    nome = input(f"Digite o {i + 1}º nome: ").strip()
    vetor_nomes.append(nome)

print("\n" + "=" * 30)
print("--- Nomes na Ordem Inversa ---")
print("=" * 30)

for nome in vetor_nomes[::-1]:
    print(nome)