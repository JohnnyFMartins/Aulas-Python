class Pessoa:
    def __init__(self, nome, idade, altura):
        self.nome = nome
        self.idade = idade
        self.altura = altura

    def apresentar(self):
        print(f'Olá meu nome é {self.nome} e tenho')
        print(f'{self.idade} anos, e tenho')
        print(f'{self.altura} de altura')
        
p1 = Pessoa("Johnny", 40, "1.70")
p1.apresentar()