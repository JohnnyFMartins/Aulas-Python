from src.controllers.produto_controller import produto_controller


def exibir_menu():
    print("\nMERCADO SUCESSO LTDA!")
    print("\n=== MENU ===")
    print("1 - Cadastrar Produto")
    print("2 - Listar")
    print("3 - Editar")
    print("4 - Deletar")
    print("5 - Buscar")
    print("0 - Sair")


def listar_produtos():
    print("\n--- Lista de Produtos ---")
    produtos = produto_controller.listar_produtos()
    if produtos:
        for produtos in produtos:
            print(
                f"ID: {produto['id']}, Nome: {produto['nome']}, Preço: {produto['preco']}, Quantidade: {produto['quantidade']}")
    else:
        print("Não existe produtos cadastrados")

def cadastrar_produtos():
    print("\n--- Cadastrar produto ---")
    nome = input("Nome: ")
    preco = input("Preço: ")
    quantidade = input("Quantidade: ")
    novo_id = produto_controller.cadastrar_produto(nome, preco, quantidade)
    print(f"Produto cadastrado com sucesso com o novo ID {novo_id}")






def main():
    cntrlProduto = produto_Controller()

    while True:
        exibir_menu()
        opc = input("Escolha uma opção: ")

        if opc == "1":
            nome = input("Nome do Produto: ")
            preco = float(input("Preço: "))
            quantidade = int(input("Quantidade: "))
            # salvariamos no banco de dados
            cntrlProduto.criar_produto(nome, preco, quantidade)

        elif opc == "2":
            # listar do banco de dados os Produtos
            produtos = cntrlProduto.listar_produtos()

            for index, produto in enumerate(produtos, 1):
                # index -> posição atual do produto listado
                # __str__ -> produto => Produtos(nome="", preco="", quantidade="")
                print(f"{index}. {produto}")

        elif opc == "3":
            Atualizar

        elif opc == "4":
            Deletar

        elif opc == "0":
            print("Saindo do sistema...")
            break

        else:
            print("Opção Invalida. Tente novamente")


if __name__ == "__main__":
    main()
