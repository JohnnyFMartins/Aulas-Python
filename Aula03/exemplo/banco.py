class ContaBancaria:
    def __init__(self, saldo):
        self.saldo = saldo

    def depositar(self, valor):
        self.saldo += valor
        print("Saldo atualizado:", self.saldo)

    def sacar(self, valor):
        if valor <= self.saldo:
            self.saldo -= valor
            print("Saldo atualizado: ",self.saldo)
            return True
        else:
            print("Não sera possivel sacar")
            return False

    def get_saldo(self):
        return self.saldo
 
ac1 = ContaBancaria(2000)
ac1.depositar(10)
ac1.sacar(20)





