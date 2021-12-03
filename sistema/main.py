from controladores.controlador_cliente import ControladorCliente
from controladores.controlador_profissao import ControladorProfissao

def main():

    #1-Cadastrar novo cliente:
    #(usado para testar antes da criacao dos controladores)
    #novo_cliente = Cliente()
    #novo_cliente.nome = "Joao"
    #novo_cliente.cpf = "00000000000"
    #novo_cliente.cidade = "Varginha"
    #novo_cliente.telefone = "32223322"
    #novo_cliente.profissao = "ator"
    #novo_cliente.salvar()

    controladorCliente = ControladorCliente()
    controladorCliente.cadastrar_cliente("Joao", "00000000001", "Varginha", "32223322", "ator")
    controladorCliente.cadastrar_cliente("Marcio", "00000000033", "Paraguaçu", "32225555", "programador")
    controladorCliente.cadastrar_cliente("Lucia", "00000000057", "Lavras", "32220001", "costureira")

    #(usado para testar antes da criacao dos controladores)
    #print("Id do Cliente:", novo_cliente.id)
    #print("Nome do Cliente:", novo_cliente.nome)
    #print("CPF do Cliente:", novo_cliente.cpf)
    #print("Cidade do Cliente:", novo_cliente.cidade)
    #print("Telefone do Cliente:", novo_cliente.telefone)
    #print("Profissão do Cliente:", novo_cliente.profissao)

    #2-Alterar/Atualizar um cliente existente:
    #OBS: Função UPDATE esta dentro da operação salvar, por isso é possivel alterar e atualizar ao mesmo tempo.
    
    #(usado para testar antes da criacao dos controladores)
    #cliente_teste = Cliente(1)
    #cliente_teste.cidade = "Lavras"
    #cliente_teste.salvar()

    controladorCliente = ControladorCliente()
    controladorCliente.atualizar_alterar_cliente(1,"Maria", "00000000002", "Belo Horizonte", "32220000", "bailarina")

    #3-Excluir um cliente:
    #Caso o cliente seja inexistente, é esperado erro "Não é possível excluir".

    #(usado para testar antes da criacao dos controladores)
    #excluir_cliente1 = Cliente(1)
    #excluir_cliente1.excluir()

    controladorCliente = ControladorCliente()
    controladorCliente.excluir_cliente(1)

    #4-Obter dados do cliente:

    controladorCliente = ControladorCliente()
    cliente = controladorCliente.obter_dado_cliente("Marcio")
    print(cliente)

    #5-Listar todos os clientes:

    controladorCliente = ControladorCliente()
    todos = controladorCliente.listar_todo_cliente()
    print(todos)

    #6-Cadastrar nova profissão:

    #(usado para testar antes da criacao dos controladores)
    #nova_profissao = Profissao()
    #nova_profissao.nome_profissao = "professor"
    #nova_profissao.salvar()

    controladorProfissao = ControladorProfissao()
    controladorProfissao.cadastrar_profissao("medico")
    controladorProfissao.cadastrar_profissao("engenheiro")

    #7-Alterar/Atualizar uma profissao existente:

    #(usado para testar antes da criacao dos controladores)
    #profissao_teste = Profissao(1)
    #profissao_teste.nome_profissao = "medico"
    #profissao_teste.salvar()

    controladorProfissao = ControladorProfissao()
    controladorProfissao.atualizar_alterar_profissao(1, "psicólogo")

    #8-Excluir uma profissao:

    #(usado para testar antes da criacao dos controladores)
    #excluir_profissao1 = Profissao(1)
    #excluir_profissao1.excluir()

    controladorProfissao = ControladorProfissao()
    controladorProfissao.excluir_profissao(1)


main()