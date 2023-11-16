from flask import Flask, jsonify, request
import json

app = Flask(__name__)

tarefas = [
    {'Id': '0',
     'Responsavel': 'Gabriel',
     'Tarefa': 'Listar tarefas',
     'Status': 'Concluido'},

    {'Id': '1',
     'Responsavel': 'Nathan',
     'Tarefa': 'Consultar Tarefa atraves do ID',
     'Status': 'Pendente'},

    {'Id': '2',
     'Responsavel': 'Dias',
     'Tarefa': 'Adicionar nova Tarefa',
     'Status': 'Pendente'},

    {'Id': '3',
     'Responsavel': 'Nathan',
     'Tarefa': 'Excluir Tarefa',
     'Status': 'Pendente'},

    {'Id': '4',
     'Responsavel': 'Nathan',
     'Tarefa': 'Editar Status das Tarefas',
     'Status': 'Pendente'}
]


@app.route('/tarefas', methods=['GET', 'POST'])
def listar_tarefas():
    if request.method == 'GET':
        return jsonify(tarefas)

    if request.method == 'POST':
        dados = json.loads(request.data)
        posicao = len(tarefas)
        dados['id'] = posicao
        tarefas.append(dados)
        mensagem = 'Novo registro inserido no ID {}'.format(posicao)
        return jsonify({'Status': 'Sucesso', 'Mensagem': mensagem})


@app.route('/tarefas/<int:id>/', methods=['GET', 'PUT', 'DELETE'])
def tarefa(id):
    if request.method == 'GET':
        try:
            response = tarefas[id]

        except IndexError:
            mensagem = 'Tarefa no ID {} não existe'.format(id)
            response = {'Status': 'erro', 'Mensagem': mensagem}

        except Exception:
            mensagem = 'Erro desconhecido'
            response = {'Status': 'erro', 'Mensagem': mensagem}

        return jsonify(response)

    elif request.method == 'PUT':
        try:
            dados = json.loads(request.data)
            tarefas[id]['Status'] = dados['Status']
            return jsonify(tarefas[id])

        except IndexError:
            mensagem = 'Tarefa não pode ser alterada pois não o ID {} não existe'.format(id)
            response = {'Status': 'erro', 'Mensagem': mensagem}
            return jsonify(response)


    elif request.method == 'DELETE':
        tarefas.pop(id)
        mensagem = 'Tarefa do ID {} excluida'.format(id)
        return jsonify({'Status': 'Sucesso', 'Mensagem': mensagem})



if __name__ == '__main__':
    app.run(debug=True)
