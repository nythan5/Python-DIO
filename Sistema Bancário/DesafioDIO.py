import datetime

saldo = 1000
limite_valor_saque = 500
extrato = ""
numero_saques_realizados = 0
LIMITE_SAQUE_DIARIOS = 3
data_hora = datetime.datetime.now()

menu = f"""

    ****Digite uma das opções abaixo para prosseguir*****

       
    [A] - Depositar
    [B] - Sacar
    [C] - Extrato
    [S] - Sair

==>"""

while True:

    opcao = input(menu).upper()

    if opcao == "A":
        valor = float(input("Informe o valor do depósito: "))

        if valor > 0:
            saldo += valor
            extrato += f"Depósito: R$ {valor:.2f} --- {data_hora.strftime('%d/%m/%Y %H:%M:%S')}\n"
            print("Depósito realizado com sucesso ---",data_hora.strftime('%d/%m/%Y %H:%M:%S'))
            
        else:
            print("Falha! Valor informado é inválido")

    elif opcao == "B":

        valor = float(input("Informe o valor do saque: "))

        excedeu_saldo = valor > saldo
        excedeu_limite_saque = valor > limite_valor_saque
        excedeu_quantidade_saques = numero_saques_realizados >= LIMITE_SAQUE_DIARIOS

        if excedeu_saldo:
            print(f"Saldo insulficiente para saque, Seu saldo atual é : {saldo:.2f}")

        elif excedeu_limite_saque:
            print(f"Valor limite de Saque Excedido ! Seu limite por saque é : {limite_valor_saque:.2f}")   

        elif excedeu_quantidade_saques:
            print(f"Você excedeu a quantidade de saque limite por dia !")     

        elif valor > 0:
            saldo -= valor 
            numero_saques_realizados += 1
            extrato += f"Saque: R$ {valor:.2f} --- {data_hora.strftime('%d/%m/%Y %H:%M:%S')}\n"
            print("Saque realizado com sucesso ---",data_hora.strftime('%d/%m/%Y %H:%M:%S'))

        else:
            print("Falha! Valor informado é inválido")

    elif opcao =="C":

        print("\n==========Extrato==========")
        print("\nNão foram realizadas movimentações."if not extrato else extrato)
        print(f"\nSaldo: R$ {saldo:.2f}")
        print("\n===========================")

    elif opcao =="S":
        break