
def menu():
    print("")
    print("Menu da Calculadora")
    print("1 - Somar")
    print("1 - Subtrair")
    print("1 - Multiplicar")
    print("1 - Dividir")
    print("9 - Sair")

def somar(n1, n2):
    return n1 + n2

def subtrair(n1, n2):
    return n1 - n2

def multiplicar(n1, n2):
    return n1 * n2

def dividir(n1, n2):
    return n1 / n2

def calculadora():
    while True:
        menu()
        opcao = int(input("Escolha uma Operação"))
        n1 = float(input("Digite o numero 1: "))
        n2 = float(input("Digite o numero 2: "))
        if opcao == 1:
            print("Resultado: ",somar(n1,n2))
        elif opcao == 2:
            print("Resultado: ",subtrair(n1,n2))
        elif opcao == 3:
            print("Resultado: ",multiplicar(n1,n2))
        elif opcao == 4:
            print("Resultado: ",dividir(n1,n2))
        else: print("Opção invalida")
            
calculadora()