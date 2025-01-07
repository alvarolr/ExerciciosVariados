#copia e cola
with open("original.txt", "r") as arquivo_original:
        conteudo = arquivo_original.read()

with open("copia.txt", "w") as arquivo_copia:
        arquivo_copia.write(conteudo)

print("O conteúdo foi copiado para 'copia.txt'.")

