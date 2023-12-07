from models import Pessoas, Usuarios
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

def insert_usuario(login, senha):
    usuario = Usuarios(login=login, senha=senha)
    usuario.save()

def consulta_usuarios():
    usuarios = Usuarios.query.all()
    print(usuarios)


if __name__ == '__main__':
    insert_pessoas()
    insert_usuario('gabriel','1234')
    #delete_pessoa()
    consulta()