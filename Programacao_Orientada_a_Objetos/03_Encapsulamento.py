class conta:
    def __init__(self,n_agencia,saldo = 0):
        self._saldo = saldo
        self.n_agencia = n_agencia

    def depositar(self,valor):
        self._saldo += valor 

    def sacar(self,valor):
        self._saldo -= valor 

    def mostrar_saldo(self):
        return self._saldo  


Conta1 = conta("0001",20)

print(Conta1.mostrar_saldo())