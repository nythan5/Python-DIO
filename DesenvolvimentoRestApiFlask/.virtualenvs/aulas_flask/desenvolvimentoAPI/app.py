from flask import Flask, jsonify, request
import json

app = Flask(__name__)

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


## Devolve ou altera e deleta um desenvolvedor pelo ID
@app.route('/dev/<int:id>/', methods=['GET', 'PUT', 'DELETE'])
def desenvolvedor(id):
    if request.method == 'GET':
        try:
            response = desenvolvedores[id]

        except IndexError:
            mensagem = 'Desenvolvedor do ID {} não existe'.format(id)
            response = {'Status': 'erro', 'Mensagem': mensagem}

        except Exception:
            mensagem = 'Erro desconhecido'
            response = {'Status': 'erro', 'Mensagem': mensagem}

        return jsonify(response)


    elif request.method == 'PUT':
        dados = json.loads(request.data)
        desenvolvedores[id] = dados
        return jsonify(dados)

    elif request.method == 'DELETE':
        desenvolvedores.pop(id)
        return jsonify({'Status': 'Sucesso', 'Mensagem': 'Registro excluido'})


# Lista todos os desenvolvedores e inclue um novo registro
@app.route('/dev/', methods=['POST', 'GET'])
def lista_desenvolvedores():
    if request.method == 'POST':
        dados = json.loads(request.data)
        posicao = len(desenvolvedores)
        dados['id'] = posicao
        desenvolvedores.append(dados)
        mensagem = 'Novo registro inserido no ID {}'.format(posicao)
        return jsonify({'Status': 'Sucesso', 'Mensagem': mensagem})

    elif request.method == 'GET':
        return jsonify(desenvolvedores)


if __name__ == '__main__':
    app.run(debug=True)
