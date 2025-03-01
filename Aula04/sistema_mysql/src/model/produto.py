import mysql.connector
from config import Config

class Produto:

    def __init__(self):
        # Iniciando a configuração do banco de dados
        self.confg = Config()

        self.connection = musql.connector.connect(
            host=self.config.MYSQL_HOST,
            user=self.config.MYSQL_USER,
            password=self.config.MYSQL_PASSWORD,
            database=self.config.MYSQL_DB
        )


        # Faz o cursos trazer o resultado em dicionarios
        self.cursor = self.connection.cursor(dictionary=True)

    def get_all_products(self):
        #Retornar a lista de todos os produtos
        query = "SELECT id, nome, preco FROM produtos"
        self.cursor.execute(query)
        return self.cursor.fetchall()

    def insert_product(self, nome, preco, quantidade):
        #Inserir um produto na tabela produtos
        query = "INSERT INT produtos (nome, preco, quantidade) VALUES (%s, %s)"
        self.cursor.execute(query,(nome, preco, quantidade))
        self.connection.commit() # confirma a transação
        return self.cursor.lastrowid

    def get_product_by_id(self, product_id):
        #Busca o produto pelo ID
        query = "SELECT id, nome, preco FROM produtos WHERE id = %s"
        self.cursor.execute(query, product_id)
        return self.cursor.fetchone()

    def delete_product_by_id(self, product_id):
        # Deletar um produto pelo id
        query = "DELE FROM produtos WHERE id = %s"
        self.cursor.execute(query, product_id)
        self.connection.commit() # confirma a transação
        return self.cursor.rowcount

    def update_product_by_id(self, product_id, nome, preco, quantidade):
        # Atualizar um produto pelo id
        query = "UPDATE produtos SET nome = %s, preco = %s WHERE id = %s, quantidade = %s"
        self.cursor.execute(query, nome, preco, quantidade, product_id)
        self.connection.commit() # confirma a transação
        return self.cursor.rowcount

    def close_connection(self):
        self.curso.close()
        self.connection.close()