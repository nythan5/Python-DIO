from datetime import date


class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade


    @classmethod
    def criar_de_data_nascimento(cls, ano, mes, dia, nome): #cls é uma referencia para a classe Pessoa
        idade = date.today().year - ano
        return cls(nome, idade)
    
    @staticmethod
    def eh_maior_idade(idade):
        return idade >= 18




p = Pessoa.criar_de_data_nascimento(1999, 10, 15, "Gabriel")
print(p.nome, p.idade)

print(Pessoa.eh_maior_idade(18))
print(Pessoa.eh_maior_idade(8))