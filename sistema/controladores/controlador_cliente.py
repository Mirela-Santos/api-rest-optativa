from modelos.cliente import Cliente

class ControladorCliente():

    def cadastrar_cliente(self, nome, cpf, cidade, telefone, profissao):
        if nome is None or cpf is None or cidade is None or telefone is None or profissao is None:
            print("Você deve preencher todos os campos cadastrais.")
            return False
            
        novo_cliente = Cliente()
        novo_cliente.nome = nome
        novo_cliente.cpf = cpf
        novo_cliente.cidade = cidade
        novo_cliente.telefone = telefone
        novo_cliente.profissao = profissao
        novo_cliente.salvar()
        pass

    def excluir_cliente(self, id):
        excluir_cliente = Cliente(id)
        excluir_cliente.excluir()
        pass

    def atualizar_alterar_cliente(self, id, nome, cpf, cidade, telefone, profissao):
        atualizar_alterar_cliente = Cliente(id)
        atualizar_alterar_cliente.nome = nome
        atualizar_alterar_cliente.cpf = cpf
        atualizar_alterar_cliente.cidade = cidade
        atualizar_alterar_cliente.telefone = telefone
        atualizar_alterar_cliente.profissao = profissao
        atualizar_alterar_cliente.salvar()
        pass

    def obter_dado_cliente(self, nome):
        listar_cliente = Cliente()
        return listar_cliente.obter_por_nome(nome)

    def listar_todo_cliente(self):
        todo_cliente = Cliente()
        return todo_cliente.obter_todos()


