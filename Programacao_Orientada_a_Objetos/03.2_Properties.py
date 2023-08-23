from datetime import date
class Pessoa:
    def __init__(self, nome, ano_nascimento):
        self._nome = nome
        self._ano_nascimento = ano_nascimento

    #propriedades servem como um porteiro que valida e 
    #forcenece informação por exemplo voce pergunta e ele 
    #te traz o valor e caso vc queira guardar valor ele vai la 
    #e guarda e tem o controle sobre a informação
    
    @property
    def nome (self):
        return self._nome 

    @property
    def idade (self):
        _ano_atual = date.today().year
        return _ano_atual - self._ano_nascimento   

pessoa1 = Pessoa ("Gabriel",1994)
print(f"Nome: {pessoa1.nome} tem {pessoa1.idade} anos")         