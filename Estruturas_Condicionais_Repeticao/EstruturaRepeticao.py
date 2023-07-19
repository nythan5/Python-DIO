# laço de repeticao FOR

texto = "Cristoffer"
VOGAIS = "AEIOU" #constante

for letra in texto:
    if letra.upper() in VOGAIS:
        print(letra)
else:
    print("#")        

# Estrutura de Range

for numero in range(11):
    print(numero)
# range(start,stop,step)

for numero in range (0,51,5):
    print(f"Tabuada do cinco {numero} ", end="") #interpolação


#Estrutura de While

opcao = -1

while opcao != 0:
    opcao = int(input("[1]Sacar \n[2]Extrato \n[0]Sair \n:"))

    if opcao == 1:
        print("Sacando")
    elif opcao == 2:
        print("Seu Extrato")
      

#Estrutura de Break

while True:
    numero = int(input("Informe um número:"))

    if numero == 10:
        break

    print(numero)
