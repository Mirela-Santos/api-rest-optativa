from flask import Flask, request, jsonify
from flask_ngrok import run_with_ngrok

from controladores.controlador_cliente import ControladorCliente
from controladores.controlador_profissao import ControladorProfissao

app = Flask(__name__)
run_with_ngrok(app)
controladorCliente = ControladorCliente()

#------------------get all clients---------------------

@app.route("/clientes")
def listar_clientes():
    todos = controladorCliente.listar_todo_cliente()
    return jsonify(todos)

#-------------------Cadastrar cliente-------------------


@app.route("/cliente",methods=["POST"])    
def cadastrarCliente():
    try:
        dados = request.get_json()
        nome = dados["nome"]
        cpf = dados["cpf"]
        cidade = dados["cidade"]
        telefone = dados["telefone"]
        profissao = dados["profissao"]
        controladorCliente.cadastrar_cliente(nome, cpf, cidade, telefone, profissao)
        return{"status": "CREATED", "mensagem": "Cadastrado com Sucesso"}
    except:
        return {"status": "ERRO", "mensagem": "Erro ao cadastrar"}

#---------------------------------Atualizar Clientes-------------------------------------------

@app.route("/cliente/<id>",methods=["PATCH"])    
def atualizarCliente(id):
    try:
        dados = request.get_json()
        nome = dados["nome"]
        cpf = dados["cpf"]
        cidade = dados["cidade"]
        telefone = dados["telefone"]
        profissao = dados["profissao"]
        controladorCliente.atualizar_alterar_cliente(id, nome, cpf, cidade, telefone, profissao)
        return{"status": "OK", "mensagem": "Cliente alterado com Sucesso"}
    except:
        return {"status": "ERRO", "mensagem": "Erro ao cadastrar"}
    
#----------------------------------Excluir Clientes---------------------------------------
@app.route("/cliente/<id>", methods=["DELETE"])
def deletarCliente(id):
    try:
        controladorCliente.excluir_cliente(id)
        return{"status": "OK", "mensagem": "Cliente deletado com Sucesso"}
    except:
        return{"status": "ERRO", "mensagem": "Erro alterando cliente"}

#----------------------------------Obter dados do cliente------------------------
@app.route("/cliente/<nome>", methods=["GET"])
def getClientByNome(nome):
    try:
        cliente = controladorCliente.obter_dado_cliente(nome)
        return jsonify(cliente)
    except:
        return {"status": "ERRO", "mensagem": "Erro ao obter dados do cliente"}


controladorProfissao = ControladorProfissao()
#---------------------------------Cadastrar profissão---------------------------
@app.route("/profissao", methods=["POST"])
def cadastrarProfissao():
    try:
        dados = request.get_json()
        profissao = dados["profissao"]
        controladorProfissao.cadastrar_profissao(profissao)
        return{"status": "OK", "mensagem": "Profissão cadastrada com Sucesso"}
    except:
        return {"status": "ERRO", "mensagem": "Erro ao cadastrar profissão"}

#---------------------Atualizar profissão--------------------------
@app.route("/profissao/<id>",methods=["PATCH"])
def atualizarProfissao(id):
    dados = request.get_json()
    profissao = dados["profissao"]
    controladorProfissao.atualizar_alterar_profissao(id, profissao)
    return{"status": "OK", "mensagem": "Profissão atualizada com Sucesso"}

#-------------------Excluir Profissão-------------------------------
@app.route("/profissao/<id>",methods=["DELETE"])
def excluirProfissao(id):
    controladorProfissao.excluir_profissao(id)
    return{"status": "OK", "mensagem": "Profissão deletada com Sucesso"}








@app.route("/",methods=["POST"])
def cadastrar_cliente():
    try:
        dados=request.get__json()
        nome = dados["nome"]
        return {"status":"OK","mensagem":"Olá{nome}"}
    except:
        return {"status":"noup","mensagem":"Deu ruim"}

app.run()