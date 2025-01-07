

#open('caminho', 'r')

#r read = leitura
#a = append adicionar
#w = escrita
#x = Criar
#r+ = leitura e escrita

# arquivo = open('linguagens.txt','w')

# print(arquivo.readable())
#print(arquivo.read())
#print(arquivo.readline())
#print(arquivo.readline())
#print(arquivo.readline())
# lista  = arquivo.readlines()
# print(lista)

# print(lista[0])

# arquivo.write('C\n')
# arquivo.write('C++\n')
# arquivo.write('Python\n')

# arquivo.close()

import os
'''
if os.path.exists('teste.txt'):
    os.remove('teste.txt')
else:
    print('arquivo não existe')
'''
#os.rmdir('novapasta')

with open('linguagens.txt', 'w') as arquivo:
    # print(arquivo.readline())
    # print(arquivo.readline())
    # print(arquivo.readline())
    # lista  = arquivo.readlines()
    # print(lista[1])
    arquivo.write('Python\n')
    arquivo.write('C++\n')
    arquivo.write('SQL\n')

try:
    with open('linguagens.txt', 'x') as arquivo:
        arquivo.write('teste')
except FileExistsError:
    print('arquivo existente')



    