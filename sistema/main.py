from controladores.controlador_cliente import ControladorCliente
from controladores.controlador_profissao import ControladorProfissao

def main():

#---------------------------------Cadastro de clientes-------------------------------------------

    controladorCliente = ControladorCliente()
    #controladorCliente.cadastrar_cliente("Sandro", "00000000001", "Varginha", "12345678", 7)

#---------------------------------Atualizar Clientes--------------------------------------------

    #controladorCliente = ControladorCliente()
    #controladorCliente.atualizar_alterar_cliente(15,"Sandro", "78445123099", "Belo Horizonte", "32220000", "bailarino")

#----------------------------------Excluir Clientes---------------------------------------

    #controladorCliente = ControladorCliente()
    #controladorCliente.excluir_cliente(13)

#----------------------------------Obter dados do cliente------------------------

    #controladorCliente = ControladorCliente()
    #cliente = controladorCliente.obter_dado_cliente(1)
    #print(cliente)

#-------------------------------- Listar todos os clientes ----------------------

    #controladorCliente = ControladorCliente()
    #todos = controladorCliente.listar_todo_cliente()
    #print(todos)

#---------------------------------Cadastrar profissão---------------------------

    #controladorProfissao = ControladorProfissao()
    #controladorProfissao.cadastrar_profissao("Programador")

#---------------------Atualizar profissão--------------------------

    #controladorProfissao = ControladorProfissao()
    #controladorProfissao.atualizar_alterar_profissao(1, "psicólogo")

#-------------------Excluir Profissão-------------------------------

    #controladorProfissao = ControladorProfissao()
    #controladorProfissao.excluir_profissao(2)


main()