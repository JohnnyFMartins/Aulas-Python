from src.controller import produto_controller

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
        for produto in produtos:
            print(f"ID: {produto['id']}, Nome: {produto['nome']}, Preço: R$ {produto['preco']:.2f}, Quantidade: {produto['quantidade']}")
    else:
        print("Não existe produtos cadastrados")

def cadastrar_produto():
    print("\n--- Cadastrar produto ---")
    nome = input("Nome: ")
    preco = float(input("Preço: "))
    quantidade = input("Quantidade: ")
    novo_id = produto_controller.cadastrar_produto(nome, preco, quantidade)
    print(f"Produto cadastrado com sucesso com o novo ID {novo_id}.")

def atualizar_produto():
    print("\nATUALIZANDO PRODUTO")

    while True:
        try:
            produto_id = input("Digite o ID do produto: ")
            id = int(produto_id)
            break
        except ValueError:
            print("ID inválido, tente novamente")

    nome = input("Digite o nome do produto: ")
    preco = input("Digite o preço do produto: ")
    quantidade = input("Digite o preço do produto: ")
    linhas = produto_controller.atualizar_produto(produto_id, nome, preco, quantidade)
    if linhas > 0: #quantidade de linhas modificadas
        print("Produto atualizado com sucesso!")
    else:
        print("Nenhum produto foi atualizado")

def main():

    while True:
        exibir_menu()
        opc = input("Escolha uma opção: ")

        if opc == "1":
            cadastrar_produto()

        elif opc == "2":
           listar_produtos()

        elif opc == "3":
            atualizar_produto()

        elif opc == "4":
            deletar_produto

        elif opc == "5":
            listar_produto_unico   

        elif opc == "0":
            print("Saindo do sistema...")
            break

        else:
            print("Opção Invalida. Tente novamente")

if __name__ == "__main__":
    main()
