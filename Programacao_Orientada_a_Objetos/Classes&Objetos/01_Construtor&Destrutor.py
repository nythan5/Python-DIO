class cachorro:
    def __init__(self, nome, cor, acordado=True): #init é sempre quando vc quer iniciar valores 
        print("Inicializando a classe...")
        self.nome = nome
        self.cor = cor
        self.acordado = acordado

    def __del__(self):
        print("Removendo a instância da classe...")


cachorro1= cachorro("Toby","Caramelo") #quando instanciamos o objeto ele ja roda o INIT 

del cachorro1 # Removendo a instancia do objeto da memoria 