'''
Exercício 7: Agenda Telefônica
Peça ao usuário para criar um dicionário que armazena nomes como chaves e números de telefone como valores. Permita adicionar, buscar e remover contatos.
'''

agenda = {}

while True:
    print("\n1. Adicionar contato")
    print("2. Buscar contato")
    print("3. Remover contato")
    print("4. Sair")

    opcao = int(input("Escolha uma opção: "))

    if opcao == 1:
        nome = input("Nome: ")
        telefone = input("Telefone: ")
        agenda[nome] = telefone
    elif opcao == 2:
        nome = input("Digite o nome do contato: ")
        if nome in agenda:
            print(f"{nome}: {agenda[nome]}")
        else:
            print("Contato não encontrado.")
    elif opcao == 3:
        nome = input("Digite o nome do contato a remover: ")
        if nome in agenda:
            agenda.pop(nome)
            print(f"Contato {nome} removido.")
        else:
            print("Contato não encontrado.")
    elif opcao == 4:
        break
    else:
        print("Opção inválida.")
