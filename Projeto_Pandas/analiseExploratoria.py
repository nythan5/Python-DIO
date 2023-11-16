import pandas as pd
import matplotlib.pyplot as plt
plt.style.use("ggplot")
pd.options.display.float_format = '{:20,.2f}'.format

# Criando nosso DataFrame
caminho = r"C:\Users\G15\Documents\Python\Estudos\Projeto_Pandas\Arquivos do Curso Pandas\datasets\A_AdventureWorks.xlsx"
df = pd.read_excel(caminho)
print(df.head(), "\n")

print("Número de Linhas/Colunas:", df.shape, "\n")
print(df.dtypes, "\n")

# Qual foi a receita total

receita_total = df["Valor Venda"].sum()
print(f"Receita total foi de R$ {receita_total:.2f}")

# Qual o custo Total?
df["custo"] = df["Custo Unitário"].mul(df["Quantidade"]) #Criando a coluna de custo
print(f"Custo total foi de R$ {df['custo'].sum()}")

# Agora que temos a receita e custo e o total, podemos achar o Lucro total
# Vamos criar uma coluna de Lucro que será Receita - Custo
df["lucro"] = df["Valor Venda"] - df["custo"]
print("Lucro total foi de R$", round(df["lucro"].sum(), 2))

# Criando uma columa com o tempo de envio
df["Tempo_envio"] = (df["Data Envio"] - df["Data Venda"]).dt.days
print(df.head(1), "\n")

# Media do tempo de Envio
media_tt = df.groupby("Marca")["Tempo_envio"].mean()
print("Media de TT/Marca", round(media_tt, 2))

# Verificando nulos
print(df.isnull().sum())

# Agrupando por ano e marca para ver o lucro
print(df.groupby([df["Data Venda"].dt.year, "Marca"])["lucro"].sum(), "\n")

# Resetando o index para exibir como DataFrame
lucro_ano = df.groupby([df["Data Venda"].dt.year, "Marca"])["lucro"].sum().reset_index()
print(lucro_ano, "\n")

# Qual o total de produtos Vendidos
print(df.groupby("Produto")["Quantidade"].sum().sort_values(ascending=False), "\n")

# Grafico do total de produtos vendidos
df.groupby("Produto")["Quantidade"].sum().sort_values(ascending=False).plot.barh(title="Total de Produtos Vendidos")
plt.xlabel("Quantidade")
plt.ylabel("Produtos")
plt.show()

# Lucro por Ano
df.groupby(df["Data Venda"].dt.year)["lucro"].sum().plot.bar(title="Lucro / Mês")
plt.xlabel("Mês")
plt.ylabel("Lucro")
plt.show()


df_2009 = df[df["Data Venda"].dt.year == 2009]

df_2009.groupby(df_2009["Data Venda"].dt.month)["lucro"].sum().plot(title="Lucro / Mês")
plt.xlabel("Mês")
plt.ylabel("Lucro")
plt.show()

# Lucro por Marca
df_2009.groupby("Marca")["lucro"].sum().plot.bar(title="Lucro / Marca")
plt.xlabel("Marca")
plt.ylabel("Lucro")
plt.xticks(rotation="horizontal") # Rotaçao da legenda X
plt.show()

# Lucro por Classe
df_2009.groupby("Classe")["lucro"].sum().plot.bar(title="Lucro / Classe")
plt.xlabel("Classe")
plt.ylabel("Lucro")
plt.xticks(rotation="horizontal")
plt.show()

# Grafico de Boxplot
plt.boxplot(df["Tempo_envio"])
plt.show()