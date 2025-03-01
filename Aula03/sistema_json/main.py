from app.controllers.clienteController import clienteController
from app.controllers.produtoController import produtoController

def exibir_menu():
    print("\n=== MENU ===")
    print("1 - Cadastrar Cliente")
    print("2 - Listar Clientes")
    print("3 - Cadastrar Produto")
    print("4 - Listar Produtos")
    print("0 - Sair do sistema")

def main():
    cntrlCliente = clienteController()
    cntrlProduto = produtoController()

    while True:
        exibir_menu()
        opc = input("Escolha uma opção: ")

        if opc == "1":
            nome = input("Nome do Cliente: ")
            email = input("E-mail: ")
            idade = int(input("Idade: "))
            # salvariamos no banco de dados
            cntrlCliente.criar_cliente(nome, email, idade)

        elif opc == "2":
            # listar do banco de dados os cliente
            clientes = cntrlCliente.listar_clientes()

            for index, cliente in enumerate(clientes, 1):
                # index -> posição atual do cliente listado
                #__str__ -> cliente => Cliente(nome="", email="", idade="")
                print(f"{index}. {cliente}")

        elif opc == "3":
            nome = input("Nome do Produto: ")
            preco = float(input("Preço: "))
            quantidade = int(input("Quantidade: "))
            # salvariamos no banco de dados
            cntrlProduto.criar_produto(nome, preco, quantidade)

        elif opc == "4":
            # listar do banco de dados os Produtos
            produtos = cntrlProduto.listar_produtos()

            for index, produto in enumerate(produtos, 1):
                # index -> posição atual do produto listado
                #__str__ -> produto => Produtos(nome="", preco="", quantidade="")
                print(f"{index}. {produto}")

        elif opc == "0":
            print("Saindo do sistema...")
            break

        else:
            print("Opção Invalida. Tente novamente")

if __name__ == "__main__":
    main()