import pandas as pd

# Dados fictícios
dados = {
    "Produto": ["Arroz", "Feijão", "Macarrão", "Óleo", "Leite", 
                "Refrigerante", "Cerveja", "Café", "Pão", "Bolo"],
    "Categoria": ["Alimentos", "Alimentos", "Alimentos", "Alimentos", "Bebidas", 
                  "Bebidas", "Bebidas", "Alimentos", "Padaria", "Padaria"],
    "Quantidade Vendida": [150, 200, 120, 90, 300, 
                           250, 180, 85, 400, 35],
    "Preço Unitário": [5.50, 7.20, 4.30, 8.90, 3.40, 
                       6.50, 4.20, 10.90, 1.20, 25.00]
}

# Criar DataFrame
df = pd.DataFrame(dados)

# Criar a coluna de receita
df["Receita"] = df["Quantidade Vendida"] * df["Preço Unitário"]

# Agrupamento por Categoria
receita_por_categoria = df.groupby("Categoria")["Receita"].sum()

# Salvar o resultado em um arquivo CSV
receita_por_categoria.to_csv("receita_por_categoria.csv")

# Salvar o resultado em um arquivo Excel
receita_por_categoria.to_excel("receita_por_categoria.xlsx", sheet_name="Resumo")

print("Arquivos salvos com sucesso!")

vendas_por_categorias = df.groupby('Categoria')['Quantidade Vendida'].sum()
print(vendas_por_categorias)
vendas_por_categorias = df.groupby(['Categoria', 'Produto'])['Quantidade Vendida'].sum()
print(vendas_por_categorias)

vendas_por_categorias.to_csv('saida.csv', index=False)
                


