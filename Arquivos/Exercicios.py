#Gravando frases em um arquivo
# Solicita 3 frases do usuário
frases = []
for i in range(1, 4):
    frase = input(f"Digite a frase {i}: ")
    frases.append(frase)

# Grava as frases em um arquivo chamado "frases.txt"
with open("linguagens.txt", "w") as arquivo:
    for frase in frases:
        arquivo.write(frase + "\n")

# Lê o conteúdo do arquivo e exibe no console
with open("linguagens.txt", "r") as arquivo:
    conteudo = arquivo.read()

print("\nConteúdo do arquivo:")
print(conteudo)





#Contando Linhas
# Lê o conteúdo de "texto.txt"
with open("linguagens.txt", "r") as arquivo:
    linhas = arquivo.readlines()
    
# Contagem de linhas
numero_linhas = len(linhas)

# Exibe os resultados
print(f"Número de linhas: {numero_linhas}")



# Solicita nomes do usuário e adiciona ao arquivo "nomes.txt"
with open("nomes.txt", "a") as arquivo:
    while True:
        nome = input("Digite um nome (ou 'sair' para terminar): ")
        if nome.lower() == "sair":
            break
        arquivo.write(nome + "\n")

print("\nNomes adicionados ao arquivo.")



#copia e cola
with open("original.txt", "r") as arquivo_original:
        conteudo = arquivo_original.read()

with open("copia.txt", "w") as arquivo_copia:
        arquivo_copia.write(conteudo)

print("O conteúdo foi copiado para 'copia.txt'.")

