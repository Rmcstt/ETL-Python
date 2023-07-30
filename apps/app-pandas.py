import pandas as pd

# Criar um DataFrame a partir de um dicionário
data = {
    'Nome': ['Alice', 'Bob', 'Charlie', 'David', 'Eva'],
    'Idade': [25, 30, 22, 28, 35],
    'Cidade': ['São Paulo', 'Rio de Janeiro', 'Belo Horizonte', 'Porto Alegre', 'Recife']
}

df = pd.DataFrame(data)

# Mostrar o conteúdo do DataFrame
print("Conteúdo do DataFrame:")
print(df)

# Filtrar os dados para mostrar apenas pessoas com idade acima de 25
df_filtrado = df[df['Idade'] > 25]

# Mostrar o DataFrame filtrado
print("\nConteúdo do DataFrame filtrado:")
print(df_filtrado)

# Calcular a média das idades
media_idades = df['Idade'].mean()
print(f"\nMédia das idades: {media_idades:.2f}")

# Adicionar uma nova coluna ao DataFrame
df['Profissão'] = ['Engenheiro', 'Advogado', 'Estudante', 'Analista', 'Médico']

# Mostrar o DataFrame com a nova coluna
print("\nConteúdo do DataFrame com nova coluna:")
print(df)

# Salvar o DataFrame em um arquivo CSV
df.to_csv('dados.csv', index=False)

# Ler o DataFrame de um arquivo CSV
df_lido = pd.read_csv('dados.csv')

# Mostrar o conteúdo do DataFrame lido do arquivo CSV
print("\nConteúdo do DataFrame lido do arquivo CSV:")
print(df_lido)
