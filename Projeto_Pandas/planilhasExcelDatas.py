import pandas as pd
import matplotlib.pyplot as plt

caminhoB = r"C:\Users\Gabriel Nathan Dias\Desktop\Python\Python-DIO\Projeto_Pandas\Arquivos do Curso Pandas\datasets\B_Aracaju.xlsx"
caminhoC = r"C:\Users\Gabriel Nathan Dias\Desktop\Python\Python-DIO\Projeto_Pandas\Arquivos do Curso Pandas\datasets\C_Fortaleza.xlsx"
caminhoE = r"C:\Users\Gabriel Nathan Dias\Desktop\Python\Python-DIO\Projeto_Pandas\Arquivos do Curso Pandas\datasets\E_Natal.xlsx"
caminhoF = r"C:\Users\Gabriel Nathan Dias\Desktop\Python\Python-DIO\Projeto_Pandas\Arquivos do Curso Pandas\datasets\F_Recife.xlsx"
caminhoG = r"C:\Users\Gabriel Nathan Dias\Desktop\Python\Python-DIO\Projeto_Pandas\Arquivos do Curso Pandas\datasets\G_Salvador.xlsx"


# Lendo os arquivos
df_Aracaju = pd.read_excel(caminhoB)
df_Fortaleza = pd.read_excel(caminhoC)
df_Natal = pd.read_excel(caminhoE)
df_Recife = pd.read_excel(caminhoF)
df_Salvador = pd.read_excel(caminhoG)

# Juntando todos os aqruivos
df = pd.concat([df_Salvador, df_Recife, df_Natal, df_Fortaleza, df_Aracaju])

# Passando a coluna data para int
df["Data"] = df["Data"].astype("int64")

# Verificando tipos das colunas
print(df.dtypes, "\n")

# Passando a coluna data para datetime
df["Data"] = pd.to_datetime(df["Data"])

# Verificando tipos das colunas
print(df.dtypes, "\n")

#####CRIANDO COLUNAS#####
df["Receita"] = df["Vendas"].mul(df["Qtde"])

print(df.head(5), "\n")

# Agrupamento por ano
print(df.groupby(df["Data"].dt.year)["Receita"].sum())

# Criando a coluna de Ano
df["Ano_Venda"] = df["Data"].dt.year

print(df.head(5), "\n")

#Extraindo o mês e o dia
df["mes_venda"], df["dia_venda"] = (df["Data"].dt.month, df["Data"].dt.day)
print(df.head(5), "\n")

#Retornando a data mais antiga
print(df["Data"].min(), "\n")

#Calculando a diferença de dias
df["diferenca_dias"] = df["Data"] - df["Data"].min()
print(df.head(5), "\n")

# Criando coluna de trimestres
df["Trimestre_Venda"] = df["Data"].dt.quarter

print(df.head(5), "\n")



# Filtrando as vendas de 2019 e do mes de março
vendas_marco_19 = df.loc[(df["Data"].dt.year == 2019) & (df["Data"].dt.month == 3)]
print(vendas_marco_19, "\n")

# Quantidade de produtos vendidos por mes
df_2019 = df[df["Ano_Venda"] == 2019]
df_2019.groupby(df_2019["mes_venda"])["Qtde"].sum().plot(marker="o")
plt.xlabel("Mês")
plt.ylabel("Total Produtos Vendidos")
plt.legend()
plt.show()

