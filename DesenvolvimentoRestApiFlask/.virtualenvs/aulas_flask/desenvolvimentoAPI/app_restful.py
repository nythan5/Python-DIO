import json
from flask import Flask, request
from flask_restful import Resource, Api

app = Flask(__name__)
api = Api(app)

desenvolvedores = [
    {
        'id': '0',
        'nome': 'Gabriel',
        'habilidades': ['Python', 'Flask']},

    {
        'id': '1',
        'nome': 'Nathan',
        'habilidades': ['Java', 'SQL']}
]


class Desenvolvedor(Resource):
    def get(self, id):
        try:
            response = desenvolvedores[id]
        except IndexError:
            mensagem = 'Desenvolvedor do ID {} não existe'.format(id)
            response = {'Status': 'erro', 'Mensagem': mensagem}

        except Exception:
            mensagem = 'Erro desconhecido'
            response = {'Status': 'erro', 'Mensagem': mensagem}

        return response

    def put(self, id):
        dados = json.loads(request.data)
        desenvolvedores[id] = dados
        return dados

    def delete(self, id):
        desenvolvedores.pop(id)
        return {'Status': 'Sucesso', 'Mensagem': 'Registro do ID {} excluido com sucesso'.format(id)}


class ListaDesenvolvedores(Resource):
    def get(self):
        return desenvolvedores

    def post(self):
        dados = json.loads(request.data)
        posicao = len(desenvolvedores)
        dados['id'] = posicao
        desenvolvedores.append(dados)
        return desenvolvedores[posicao]


# rotas aqui
api.add_resource(Desenvolvedor, '/dev/<int:id>')
api.add_resource(ListaDesenvolvedores, '/dev')

if __name__ == '__main__':
    app.run(debug=True)
