import mysql.connector
from Aula07.sistema_mvc.config import Config

class Produto:

    def __init__(self):
        # Iniciando a configuração do banco de dados
        self.config = Config()

        self.connection = mysql.connector.connect(
            host=self.config.MYSQL_HOST,
            user=self.config.MYSQL_USER,
            password=self.config.MYSQL_PASSWORD,
            database=self.config.MYSQL_DB,
        )
        # Faz o cursos trazer o resultado em dicionarios
        self.cursor = self.connection.cursor(dictionary=True)

    def get_all_products(self):
        #Retornar a lista de todos os produtos
        query = "SELECT id, nome, preco, quantidade FROM produtos"
        self.cursor.execute(query)
        return self.cursor.fetchall()

    def insert_produtos(self, nome, preco, quantidade):
        #Inserir um produto na tabela produtos
        query = "INSERT INTO produtos (nome, preco, quantidade) VALUES (%s, %s, %s)"
        self.cursor.execute(query,(nome, preco, quantidade))
        self.connection.commit() # confirma a transação
        return self.cursor.lastrowid

    def get_product_by_id(self, produto_id):
        #Busca o produto pelo ID
        query = "SELECT * WHERE id = %s"
        self.cursor.execute(query, produto_id)
        return self.cursor.fetchone()

    def delete_product_by_id(self, produto_id):
        # Deletar um produto pelo id
        query = "DELE FROM produtos WHERE id = %s"
        self.cursor.execute(query, produto_id)
        self.connection.commit() # confirma a transação
        return self.cursor.rowcount

    def update_produto_by_id(self, produto_id, nome, preco, quantidade):
        # Atualizar um produto pelo id
        query = "UPDATE produtos SET nome = %s, preco = %s , quantidade = %s WHERE id = %s"
        self.cursor.execute(query, (nome, preco, quantidade, produto_id))
        self.connection.commit() # confirma a transação
        return self.cursor.rowcount

    def close_connection(self):
        self.cursor.close()
        self.connection.close()