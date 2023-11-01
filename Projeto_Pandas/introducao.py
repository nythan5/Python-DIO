import pandas as pd





caminho = r"C:\Users\Gabriel Nathan Dias\Desktop\Python\Python-DIO\Projeto_Pandas\Arquivos do Curso Pandas\datasets\D_Gapminder.csv"

df = pd.read_csv(caminho, sep=';') # Colocando o separador por ;

# Renomeando o nome das colunas lembrando que é um dict ou seja Chave e Valor
df = df.rename(columns={"country": "Pais", "continent": "Continente", "Year": "Ano",
                        "lifeExp": "Exp de Vida", "pop": "População", "gdpPercap": "Renda Percapta"})

# Printando apenas as 5 primeiras linhas para exibir tipo mais linhas é só colocar entre o ()
print(df.head(),"\n")

# Printando o final do DF
print(df.tail(),"\n")

# Describe tipo umas estatisticas pra gente
print(df.describe(),"\n")

# Printando as informações de uma coluna
print(df["Continente"].unique(),"\n")

# Dados da Oceania
df_oceania = df.loc[df["Continente"] == "Oceania"]
print(df_oceania["Pais"].unique(),"\n")

# Quantos paises tem por continente
print(df.groupby("Continente")["Pais"].nunique())

# Qual a exp de vida media para cada ano
print(df.groupby(["year"])["Exp de Vida"].mean())

# Qual a exp de vida media por ano para cada pais
print(df.groupby(["Pais", "year"])["Renda Percapta"].mean())



#print("Total de Linhas e Colunas", df.shape)

#print("Nome das Colunas", df.columns)