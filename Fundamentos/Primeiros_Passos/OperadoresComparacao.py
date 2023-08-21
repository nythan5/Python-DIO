saldo = 1000
saque = 1300
limite = 200
conta_especial = False
Liberacao_Saque = False


if(saldo >= saque and saque <=limite ) or (conta_especial and saldo >=limite):
    Liberacao_Saque = True

if Liberacao_Saque :
    print ("Saque liberado!")
    
else:
     print("Saque nao liberado")