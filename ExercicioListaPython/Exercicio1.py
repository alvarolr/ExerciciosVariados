'''
Exercício 1: Manipulação de Lista
Crie uma lista com 5 números fornecidos pelo usuário e exiba:

O maior número.
O menor número.
A soma de todos os números.

'''

numeros = []

for i in range(5):
    numero = int(input(f"Digite o número {i + 1}: "))
    numeros.append(numero)

print(f"Maior número: {max(numeros)}")
print(f"Menor número: {min(numeros)}")
print(f"Soma dos números: {sum(numeros)}")
