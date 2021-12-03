from base.modelo import Modelo

class Profissao(Modelo):
    Tabela = "profissao"

    def __init__(self, id=None):
        super().__init__(self.Tabela);
        self.id = id;
        if id:
            dado = self.obter_por_id(id)
            if dado:
                self.nome_profissao = dado[1];
            else:
                self.id = None;
                self.nome_profissao = None;
        else:
            self.nome_profissao = None;
    
    def salvar(self):
        try:
            if self.id:
                instrucao = "UPDATE {tabela} SET nome_profissao=%s WHERE id=%s".format(tabela =self.Tabela)
                self.obter_cursor().execute(instrucao, [self.nome_profissao,self.id])
            else:
                instrucao = "INSERT INTO {tabela} (nome_profissao) VALUES (%s)".format(tabela =self.Tabela)
                self.obter_cursor().execute(instrucao, [self.nome_profissao])
                self.id = self.obter_cursor().lastrowid
            return True
        except:
            print("Ocorreu um erro ao executar", self.obter_cursor()._last_executed)
            return False

    def excluir(self):
        if self.id:
            self.excluir_por_id(self.id)
            return True
        else:
            print(f"Não é possível excluir. {self.id}")
            return False