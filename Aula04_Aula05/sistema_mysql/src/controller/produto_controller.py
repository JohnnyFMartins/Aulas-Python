from ..model.produto import Produto

def listar_produtos():
    #Retorna a lista de todos os produtos (dict)
    model = Produto()
    produtos = model.get_all_products()
    model.close_connection()
    return produtos

def cadastrar_produto(nome, preco, quantidade):
    # Cadastrar produto no banco
    model = Produto()
    novo_id = model.insert_produtos(nome, preco, quantidade)
    model.close_connection()
    return novo_id

def atualizar_produto(produto_id, nome, preco, quantidade):
    model = Produto()
    linhas_afetadas = model.update_produto_by_id(produto_id, nome, preco, quantidade)
    model.close_connection()
    return linhas_afetadas

def remover_produto(produto_id):
    model = Produto()
    linhas_afetadas = model.delete_produto_by_id(produto_id)
    model.close_connection()
    return linhas_afetadas

def obter_produto(produto_id):
    model = Produto()
    linhas_afetadas = model.get_produto_by_id(produto_id)
    model.close_connection()
    return linhas_afetadas