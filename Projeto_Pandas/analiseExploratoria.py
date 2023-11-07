import pandas as pd
import matplotlib.pyplot as plt
plt.style.use("ggplot")

# Criando nosso DataFrame
caminho = r"C:\Users\Gabriel Nathan Dias\Desktop\Python\Python-DIO\Projeto_Pandas\Arquivos do Curso Pandas\datasets\A_AdventureWorks.xlsx"
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

