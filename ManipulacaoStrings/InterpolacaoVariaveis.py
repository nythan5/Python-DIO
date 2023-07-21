#Old style %

nome = "Gabriel"
idade = 23
linguagem ="Python"
Saldo = 45.235

dados = {"nome":"Cristiane","idade":"24"}

print("Olá, me chamo %s. Eu tenho %d e estou estudando %s." % (nome,idade,linguagem))

#format style

print("Olá, me chamo {}. Eu tenho {} e estou estudando {}." .format(nome,idade,linguagem))

#format com indice

print("Olá, me chamo {0}. Eu tenho {1} e estou estudando {2}." .format(nome,idade,linguagem)) #podendo alterar ordem e repetir variaveis quantas vezes necessário

print("Olá, me chamo {nome}. Eu tenho {idade} e estou estudando {linguagem}." .format(nome = nome,idade=idade,linguagem=linguagem)) #podendo alterar ordem e repetir variaveis quantas vezes necessário

print("nome: {nome} idade: {idade}".format(**dados))

# F string

print(f"Nome: {nome} Idade: {idade}")

print(f"Nome: {nome} Idade: {idade} Dinheiro em conta:{Saldo:.2f}") #formatado o numero de casas dps ou antes da virgula
