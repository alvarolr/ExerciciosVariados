'''
Exercício 3: Ordenando Nomes
Peça ao usuário 5 nomes e exiba-os em ordem alfabética.
'''

nomes = []

for i in range(5):
    nome = input("Digite um nome: ")
    nomes.append(nome)

nomes.sort()
print("Nomes em ordem alfabética:", nomes)
