def sacar(valor):
    saldo = 500
    if saldo >= valor:
        print("Valor sacado!")
        saldo -= valor
        print("Saldo restante =",saldo)
    else:
        print("Valor não disponivel")


def depositar(valor):  
    saldo = 500   
    saldo += valor
    print("Saldo atual",saldo)


depositar(100)
sacar(150)