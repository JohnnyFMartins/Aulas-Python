class Cliente:

    def __init__(self, id, nome, email, idade):
        self.id = id
        self.nome = nome
        self.email = email
        self.idade = idade

    def __str__(self):
        return f"Cliente(nome={self.nome}, email={self.email}, idade={self.idade})"