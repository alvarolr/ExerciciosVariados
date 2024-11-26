'''
Exercício 2: Tabuada com Lista
Crie uma lista com os números de 1 a 10 e exiba a tabuada de um número fornecido pelo usuário.

'''

tabuada = []
numero = int(input("Digite um número para ver a tabuada: "))

for i in range(1, 11):
    tabuada.append(numero * i)

print(f"Tabuada de {numero}: {tabuada}")
