import pandas as pd

caminhoB = r"C:\Users\G15\Documents\Python\Estudos\Projeto_Pandas\Arquivos do Curso Pandas\datasets\B_Aracaju.xlsx"
caminhoC = r"C:\Users\G15\Documents\Python\Estudos\Projeto_Pandas\Arquivos do Curso Pandas\datasets\C_Fortaleza.xlsx"
caminhoE = r"C:\Users\G15\Documents\Python\Estudos\Projeto_Pandas\Arquivos do Curso Pandas\datasets\E_Natal.xlsx"
caminhoF = r"C:\Users\G15\Documents\Python\Estudos\Projeto_Pandas\Arquivos do Curso Pandas\datasets\F_Recife.xlsx"
caminhoG = r"C:\Users\G15\Documents\Python\Estudos\Projeto_Pandas\Arquivos do Curso Pandas\datasets\G_Salvador.xlsx"


# Lendo os arquivos
df_Aracaju = pd.read_excel(caminhoB)
df_Fortaleza = pd.read_excel(caminhoC)
df_Natal = pd.read_excel(caminhoE)
df_Recife = pd.read_excel(caminhoF)
df_Salvador = pd.read_excel(caminhoG)

# Juntando todos os aqruivos

df = pd.concat([df_Salvador, df_Recife, df_Natal, df_Fortaleza, df_Aracaju])

# Exibindo as 5 primeiras linhas
print(df.head(), "\n")

# Exibindo as 5 ultimas linhas
print(df.tail(), "\n")

# Exibindo uma amostra
print(df.sample(10), "\n")

# Exibindo os tipos das colunas da tabela
print(df.dtypes, "\n")

# Alterando tipo de dados
df["LojaID"] = df["LojaID"].astype("object")

# Exibindo os tipos das colunas da tabela
print(df.dtypes, "\n")

# Consultando linhas com valores faltantes
print(df.isnull().sum(), "\n")

# Substituindo os valores nulos pela media
df["Vendas"].fillna(df["Vendas"].mean(), inplace=True)

# Substituindo os valores nulos por 0
df["Vendas"].fillna(0, inplace=True)

# Apagando as linhas nulas
df.dropna(inplace=True)

# Apagando as linhas com valores nulos com base apenas em uma coluna
df.dropna(subset=["Vendas"], inplace=True)

# Apagando as linhas com valores nulos em todas as colunas
df.dropna(how="all", inplace=True)

#####CRIANDO COLUNAS#####
df["Receita"] = df["Vendas"].mul(df["Qtde"])

print(df.head(), "\n")

# Retornando maior receita e menor receita
print(df["Receita"].max(), "\n")
print(df["Receita"].min(), "\n")

# Retornar top  ou top -5
print(df.nlargest(5, ["Receita"]), "\n")
print(df.nsmallest(5, ["Receita"]), "\n")

# Agrupando receita por cidade
print(df.groupby("Cidade")["Receita"].sum())

# Ordenando essa receita
print(df.sort_values("Receita", ascending=False).head(10))




