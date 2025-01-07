# Solicita nomes do usuário e adiciona ao arquivo "nomes.txt"
with open("linguagens.txt", "a") as arquivo:
    while True:
        nome = input("Digite um nome (ou 'sair' para terminar): ")
        if nome.lower() == "sair":
            break
        arquivo.write(nome + "\n")

print("\nNomes adicionados ao arquivo.")
