'''
Simulando um Carrinho de Compras
Crie um programa que simula um carrinho de compras. Permita que o usuário adicione produtos à lista, veja todos os itens e remova produtos específicos.
'''

carrinho = []

while True:
    print("\n1. Adicionar produto")
    print("2. Ver carrinho")
    print("3. Remover produto")
    print("4. Sair")

    opcao = int(input("Escolha uma opção: "))

    if opcao == 1:
        produto = input("Digite o nome do produto: ")
        carrinho.append(produto)
    elif opcao == 2:
        print("Carrinho:", carrinho)
    elif opcao == 3:
        produto = input("Digite o nome do produto a remover: ")
        if produto in carrinho:
            carrinho.remove(produto)
        else:
            print("Produto não encontrado.")
    elif opcao == 4:
        break
    else:
        print("Opção inválida.")
