class bicicleta :
    def __init__(self,cor,modelo,valor,aro): #self é o construtor
        self.cor = cor  # isso que é self. são os atributos da classe
        self.modelo = modelo
        self.aro = aro
        self.valor = valor        
        self.marcha = 0


    def buzinar(self): #metodo é identico a funcao
        print("Bi! Bi!")

    def grau(self):
        print("BOLOLOLO")

    def aumentar_marcha(_self,n_marcha):
        if n_marcha > _self.marcha:
            print("Marcha trocada")
        else:
            print("Tente uma marcha seguinte")

    def diminuir_marcha(_self,n_marcha):
        if n_marcha < _self.marcha:
            print("Marcha Reduzida")
        else:
            print("Tente uma marcha anterior")        
    

    def __str__(self):
        return f"{self.__class__.__name__}:{', '.join([f'{chave}={valor}' for chave,valor in self.__dict__.items()])}"
    

bike1 = bicicleta("Vermelha","BMX",1000,"29")

bike2 = bicicleta("Azul","GTS",2000,"29")

#print(bike1.cor)

#bike1.grau() # este cara é igual a linha debaixo

#bicicleta.grau(bike2)

#print(bike1) # aqui estamos utilizando o metodo STR

bike1.aumentar_marcha(1)
bike1.aumentar_marcha(2)
bike1.diminuir_marcha(-1)