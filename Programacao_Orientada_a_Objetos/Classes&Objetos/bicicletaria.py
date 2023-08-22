class bicicleta :
    def __init__(self,cor,modelo,tamanho,valor):
        self.cor = cor
        self.modelo = modelo
        self.tamanho = tamanho
        self.valor = valor

    def buzinar(self):
        print("Bi! Bi!")

    def grau(self):
        print("BOLOLOLO")

    def __str__(self):
        return f"{self.__class__.__name__}:{','.join([f'{chave}={valor}' for chave,valor in self.__dict__.items()])}"
    

bike = bicicleta("Vermelha","BMX","29",1000)

print(bike.cor)

bike.grau()