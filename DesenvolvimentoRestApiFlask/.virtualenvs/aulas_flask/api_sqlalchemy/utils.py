from models import Pessoas
def insert_pessoas():
    pessoa = Pessoas(nome= 'Nathan', idade=23)
    pessoa.save()
    print(f'Inserido no Banco - {pessoa}')
def consulta():
    pessoas = Pessoas.query.all()
    print(pessoas)
    pessoa = Pessoas.query.filter_by(nome='Nathan').first()
    print(pessoa.idade)

def uptade_pessoa():
    pessoa = Pessoas.query.filter_by(nome='Nathan').first()
    pessoa.idade = 15
    pessoa.save()

def delete_pessoa():
    pessoa = Pessoas.query.filter_by(nome="Gabriel").first()
    pessoa.delete()

if __name__ == '__main__':
    insert_pessoas()
    #delete_pessoa()
    consulta()