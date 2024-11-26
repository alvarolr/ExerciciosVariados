'''
Exercício 6: Cadastro de Aluno
Peça ao aluno para criar um dicionário com as informações de um aluno (nome, idade, nota). Depois, exiba os dados formatados.
'''

aluno = {
    "nome": input("Digite o nome do aluno: "),
    "idade": int(input("Digite a idade do aluno: ")),
    "nota": float(input("Digite a nota do aluno: "))
}

print(f"O aluno {aluno['nome']} tem {aluno['idade']} anos e tirou nota {aluno['nota']:.2f}.")
