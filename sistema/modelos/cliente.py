from base.modelo import Modelo

class Cliente(Modelo):
    Tabela = "cliente"

    def __init__(self, id=None):
        super().__init__(self.Tabela);
        self.id = id;
        if id:
            dado = self.obter_por_id(id)
            if dado:
                self.nome = dado[1];
                self.cpf = dado[2];
                self.cidade = dado[3];
                self.telefone = dado[4];
                self.profissao = dado[5];
            else:
                self.id = None;
                self.nome = None;
                self.cpf = None;
                self.cidade = None;
                self.telefone = None;
                self.profissao = None;
        else:
            self.nome = None;
            self.cpf = None;
            self.cidade = None;
            self.telefone = None;
            self.profissao = None;
    
    def salvar(self):
        try:
            if self.id:
                instrucao = "UPDATE {tabela} SET nome=%s,cpf=%s,cidade=%s,telefone=%s,profissao=%s WHERE id=%s".format(tabela =self.Tabela)
                self.obter_cursor().execute(instrucao, [self.nome,self.cpf,self.cidade,self.telefone,self.profissao,self.id])
            else:
                instrucao = "INSERT INTO {tabela} (nome,cpf,cidade,telefone,profissao) VALUES (%s, %s, %s,%s,%s)".format(tabela =self.Tabela)
                self.obter_cursor().execute(instrucao, [self.nome,self.cpf,self.cidade,self.telefone,self.profissao])
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

    def obter_por_nome(self, nome):
        try:
            instrucao = "SELECT * FROM {tabela} WHERE nome LIKE %s".format(tabela = self.Tabela)
            self.__cursor.execute(instrucao, nome)
            resultado = self.__cursor.fetchone()
            return resultado
        except:
            print("Erro ao executar.", self.__cursor._last_executed)
            return None
