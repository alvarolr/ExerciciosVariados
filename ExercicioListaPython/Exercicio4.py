'''
Exercício 5: Removendo Elementos
Crie um programa que solicita ao usuário para preencher uma lista com 5 números e, em seguida, remova um número escolhido pelo usuário.
'''

numeros = []

for i in range(5):
    numero = int(input("Digite um número: "))
    numeros.append(numero)

print("Lista original:", numeros)

remover = int(input("Digite um número para remover: "))
if remover in numeros:
    numeros.remove(remover)
    print("Nova lista:", numeros)
else:
    print("Número não encontrado na lista.")
