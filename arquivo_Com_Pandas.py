import pandas as pd

#lendo o arquivo CSV
df = pd.read_csv('dados_vendas.csv')
print(df.head())
#print(df.info())
#print(df.describe())
print(df['Produto'])
maiores = df[df['Data de Venda'] > '2023-02-01']
print(maiores)

vendas_por_categorias = df.groupby('Categoria')['Quantidade Vendida'].sum()
print(vendas_por_categorias)
vendas_por_categorias = df.groupby(['Categoria', 'Produto'])['Quantidade Vendida'].sum()
print(vendas_por_categorias)

df['receita'] = df['Quantidade Vendida'] * df['Preço Unitário']

receita_por_categoria = df.groupby('Categoria')['receita'].sum()
print(receita_por_categoria)
print(df.columns)
vendas_por_categorias.to_csv('saida.csv', index=False)
                
