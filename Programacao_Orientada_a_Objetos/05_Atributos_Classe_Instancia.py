class Estudante:
    escola = "Digital Inovation One" # esta variavel de classe ela altera todos os objetos criados  

    def __init__(self,nome,matricula): # já as variaveis de instancia ela mudam apenas na instancia que voce mudou 
        self.nome = nome
        self.matricula = matricula

    def __str__(self) -> str:
        return f"{self.nome} - {self.matricula} - {self.escola}"
    

def mostrar_valores(*objs):
        for obj in objs:
            print(obj)


aluno1 = Estudante("Gabriel",1)
aluno2 = Estudante("Cris",2)    

mostrar_valores(aluno1,aluno2)

aluno2.matricula = 3
Estudante.escola = "DIO"

mostrar_valores(aluno1,aluno2)