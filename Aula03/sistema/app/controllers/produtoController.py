from ..models.produto import Produto
from ..database.database import bancoFake

class produtoController:
    def __init__(self):
        # conexao com o banco
        self.db = bancoFake()

    def criar_produto(self, nome, preco, quantidade):
        # Criar o objeto cliente  salvar no banco
        novo_produto = Produto(nome, preco, quantidade)
        # converter para dict (JSON)
        dict_produto = {
            "nome": novo_produto.nome,
            "Preco": novo_produto.preco,
            "quantidade": novo_produto.quantidade
        }
        # salvar no banco
        self.db.adicionar_produto(dict_produto)
        print("Produto cadastrado com sucesso!")

    def listar_produtos(self):
        # retorna um alista com todos os produtos cadastrados
        return self.db.listar_produtos()