from base.modelo import Modelo

class Cliente(Modelo):
    Tabela = "cliente"

    def __init__(self):
        super().__init__(self.Tabela);
        self.id = None;
        self.nome = None;
        self.cpf = None;
        self.cidade = None;
        self.telefone = None;
        self.profissao = None
    
    def salvar(self):
        try:
            instrucao = "INSERT INTO {tabela} (nome,cpf,cidade,telefone,profissao) VALUES (%s, %s, %s,%s,%s)".format(tabela =self.Tabela)
            self.obter_cursor().execute(instrucao, [self.nome,self.cpf,self.cidade,self.telefone,self.profissao])
            return True
        except:
            print("Ocorreu um erro ao executar", self.obter_cursor()._last_executed)
            return False