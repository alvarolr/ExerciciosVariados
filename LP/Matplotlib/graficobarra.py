from matplotlib import pyplot as plt

# Dados
produtos = ['Arroz', 'Feijão', 'Macarrão', 'Óleo', 'Leite']
quantidades = [150, 200, 120, 90, 300]

# Criando o gráfico
plt.bar(produtos, quantidades, color='skyblue')

plt.bar_label(plt.bar(produtos, quantidades), label_type='edge', padding=5)


# Adicionando título e rótulos
plt.title('Quantidade Vendida por Produto')
plt.xlabel('Produtos')
plt.ylabel('Quantidade Vendida')

# Exibindo o gráfico
plt.show()
