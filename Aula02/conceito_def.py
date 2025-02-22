#def -> função


def carro_johnny():
    print("Corsa 1.4 premium")


carro_johnny()

def escrever_carro(nome):
    print(nome)

escrever_carro("Honda Civic")

def somar_numeros(num1, num2):
    return num1 + num2
   
resultado = somar_numeros(4,4)
print("O resultados é: ", resultado)

def verificarIdade(idade):
    if idade >= 18:
        return "Pode ver o filme"
    else:
        return "Não pode ver o filme"


idade = int(input("digite sua idade: "))
resultado = verificarIdade(idade)
print(resultado)

