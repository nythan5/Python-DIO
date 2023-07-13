def sacar(valor):
    saldo = 500
    if saldo >= valor:
        print("Valor sacado!")
        saldo -= valor
        print("Saldo restante =",saldo)
    else:
        print("Valor não disponivel")
	
	
# utilizamos o if/elif e else como switch case em outras linguagens

"""
bike = str(input("Escolha um modelo de Bike: "))

if bike == 'Hero':
	print("bike is Hero")

elif bike == "Suzuki":
	print("bike is Suzuki")

elif bike == "Yamaha":
	print("bike is Yamaha")

else:
	print("Escolha entre Suzuki/Yamaha ou Hero")
	
"""


# if elif else aninhado

Saldo = 2000
saque = 2500
cheque_especial = 450

conta_universitaria = False
conta_normal = False

if conta_normal:
	if Saldo >= saque:
		print ("Saque Realizado!")
	elif saque <= (Saldo+cheque_especial):
		print("Saque realizado com uso do Cheque Especial!")
	else:
		print("Não há saldo sulficiente!")		
elif conta_universitaria:
	if Saldo >= saque:
		print("Saque Realizado!")
	else:
		print("Saldo insulficiente!")	
else:
	print("Nenhuma conta reconhecida!")				


# if ternário

status = "Sucesso" if Saldo >= saque else "Falha"

print(f"{status} ao realizado o saque!")