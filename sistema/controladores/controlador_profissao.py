from modelos.profissao import Profissao

class ControladorProfissao():

    def cadastrar_profissao(self, nome_profissao):
        if nome_profissao is None:
            print("Você deve preencher o nome de sua profissão.")
            return False
            
        novo_profissao = Profissao()
        novo_profissao.nome_profissao = nome_profissao
        novo_profissao.salvar()
        pass

    def excluir_profissao(self, id):
        excluir_profissao = Profissao(id)
        excluir_profissao.excluir()
        pass

    def atualizar_alterar_profissao(self, id, nome_profissao):
        atualizar_alterar_profissao = Profissao(id)
        atualizar_alterar_profissao.nome_profissao = nome_profissao
        atualizar_alterar_profissao.salvar()
        pass