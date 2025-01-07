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