class veiculo:
    def __init__(self,cor,marca,combustivel,fabricacao,placa):
        self.cor = cor
        self.marca = marca
        self.combustivel = combustivel
        self.fabricacao = fabricacao
        self.placa = placa

        def ligar (self):
            print("Motor Ligado")
        

class motocicleta(veiculo):
    def __init__(self, cor, marca, combustivel, fabricacao, placa, cilindrada):
        super().__init__(cor, marca, combustivel, fabricacao, placa)
        self.cilindrada = cilindrada
       


MotoYamaha = motocicleta("preto","Yamaha","Gasolina",2020,"GES-1234","150cc")


print(MotoYamaha.placa)
