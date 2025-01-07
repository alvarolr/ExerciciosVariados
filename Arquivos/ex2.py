#Contando Linhas
# Lê o conteúdo de "texto.txt"
with open("linguagens.txt", "r") as arquivo:
    linhas = arquivo.readlines()
    
# Contagem de linhas
numero_linhas = len(linhas)

# Exibe os resultados
print(f"Número de linhas: {numero_linhas}")