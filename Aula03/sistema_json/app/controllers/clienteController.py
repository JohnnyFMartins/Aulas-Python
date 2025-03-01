from ..models.cliente import Cliente
from ..database.database import bancoFake

class clienteController:
    def __init__(self):
        # conexao com o banco
        self.db = bancoFake()

    def criar_cliente(self, nome, email, idade):
        # Criar o objeto cliente  salvar no banco
        novo_id = self.db.gerar_id_cliente()
        novo_cliente = Cliente(novo_id, nome, email, idade)
        # converter para dict (JSON)
        dict_cliente = {
            "nome": novo_cliente.nome,
            "email": novo_cliente.email,
            "idade": novo_cliente.idade
        }
        # salvar no banco
        self.db.adicionar_cliente(dict_cliente)
        print("Cliente cadastrado com sucesso!")

    def listar_clientes(self):
        # retorna um alista com todos os clientes cadastrados
        return self.db.listar_clientes()

