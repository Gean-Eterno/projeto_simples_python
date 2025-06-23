# Mensagem de boas-vindas com o nome do desenvolvedor
print("Seja bem-vindo à livraria do Gean Rodrigues")

# Lista que armazenará todos os livros cadastrados (como dicionários)
lista_livro = []

# Variável que controla o ID global dos livros
id_global = 0

# Função para cadastrar um novo livro com base no ID recebido
def cadastrar_livro(id):
    # Solicita os dados do livro ao usuário
    nome = input("Digite o nome do livro: ")
    autor = input("Digite o autor do livro: ")
    editora = input("Digite a editora do livro: ")

    # Cria um dicionário com os dados do livro
    livro = {
        "id": id,
        "nome": nome,
        "autor": autor,
        "editora": editora,
    }

    # Adiciona o dicionário à lista de livros
    lista_livro.append(livro)

# Função para consultar os livros cadastrados
def consultar_livro():
    while True:
        # Exibe o menu de consulta
        print("Escolha a opção desejada:")
        print("1. Consultar todos os livros")
        print("2. Consultar livro por ID")
        print("3. Consultar livro por autor")
        print("4. Retornar ao menu")

        opcao = input("Digite a opção desejada: ")

        # Caso o usuário deseje consultar todos os livros
        if opcao == "1":
            for livro in lista_livro:
                print("ID:", livro["id"])
                print("Nome:", livro["nome"])
                print("Autor:", livro["autor"])
                print("Editora:", livro["editora"])

        # Caso o usuário deseje consultar por ID
        elif opcao == "2":
            id_desejado = int(input("Digite o ID do livro: "))
            encontrado = False
            for livro in lista_livro:
                if livro["id"] == id_desejado:
                    print("Livro encontrado:")
                    print(f"ID: {livro['id']}")
                    print(f"Nome: {livro['nome']}")
                    print(f"Autor: {livro['autor']}")
                    print(f"Editora: {livro['editora']}")
                    encontrado = True
                    break
            if not encontrado:
                print("Essa ID não corresponde a nenhum livro.")

        # Caso o usuário deseje consultar por autor
        elif opcao == "3":
            autor_desejado = input("Digite o nome do autor: ")
            encontrado = False
            for livro in lista_livro:
                if livro["autor"].lower() == autor_desejado.lower():
                    print("Livro encontrado:")
                    print(f"ID: {livro['id']}")
                    print(f"Nome: {livro['nome']}")
                    print(f"Autor: {livro['autor']}")
                    print(f"Editora: {livro['editora']}")
                    print("-----------------------------")
                    encontrado = True
            if not encontrado:
                print("Nenhum livro encontrado para esse autor.")

        # Retorna ao menu principal
        elif opcao == "4":
            break

        # Caso a opção não seja válida
        else:
            print("Opção inválida. Tente novamente.")

# Função responsável por remover um livro da lista
def remover_livro():
    id_remover = int(input("Digite o ID do livro que deseja remover: "))
    encontrado = False
    for livro in lista_livro:
        if livro["id"] == id_remover:
            lista_livro.remove(livro)
            print(f"Livro com o ID {id_remover} removido com sucesso.")
            encontrado = True
            break
    if not encontrado:
        print("Livro não encontrado.")

# Menu principal do programa (laço principal)
while True:
    # Mensagem de boas-vindas com o nome do desenvolvedor
    print("Seja bem-vindo à livraria do Gean Rodrigues")

    # Lista que armazenará todos os livros cadastrados (como dicionários)
    lista_livro = []

    # Variável que controla o ID global dos livros
    id_global = 0


    # Função para cadastrar um novo livro com base no ID recebido
    def cadastrar_livro(id):
        # Solicita os dados do livro ao usuário
        nome = input("Digite o nome do livro: ")
        autor = input("Digite o autor do livro: ")
        editora = input("Digite a editora do livro: ")

        # Cria um dicionário com os dados do livro
        livro = {
            "id": id,
            "nome": nome,
            "autor": autor,
            "editora": editora,
        }

        # Adiciona o dicionário à lista de livros
        lista_livro.append(livro)

        # Função para consultar os livros cadastrados


    def consultar_livro():
        while True:
            # Exibe o menu de consulta
            print("Escolha a opção desejada:")
            print("1. Consultar todos os livros")
            print("2. Consultar livro por ID")
            print("3. Consultar livro por autor")
            print("4. Retornar ao menu")

            opcao = input("Digite a opção desejada: ")

            # Caso o usuário deseje consultar todos os livros
            if opcao == "1":
                for livro in lista_livro:
                    print("ID:", livro["id"])
                    print("Nome:", livro["nome"])
                    print("Autor:", livro["autor"])
                    print("Editora:", livro["editora"])

                    # Caso o usuário deseje consultar por ID
            elif opcao == "2":
                id_desejado = int(input("Digite o ID do livro: "))
                encontrado = False
                for livro in lista_livro:
                    if livro["id"] == id_desejado:
                        print("Livro encontrado:")
                        print(f"ID: {livro['id']}")
                        print(f"Nome: {livro['nome']}")
                        print(f"Autor: {livro['autor']}")
                        print(f"Editora: {livro['editora']}")
                        encontrado = True
                        break
                if not encontrado:
                    print("Essa ID não corresponde a nenhum livro.")

                    # Caso o usuário deseje consultar por autor
            elif opcao == "3":
                autor_desejado = input("Digite o nome do autor: ")
                encontrado = False
                for livro in lista_livro:
                    if livro["autor"].lower() == autor_desejado.lower():
                        print("Livro encontrado:")
                        print(f"ID: {livro['id']}")
                        print(f"Nome: {livro['nome']}")
                        print(f"Autor: {livro['autor']}")
                        print(f"Editora: {livro['editora']}")
                        print("-----------------------------")
                        encontrado = True
                if not encontrado:
                    print("Nenhum livro encontrado para esse autor.")

                    # Retorna ao menu principal
            elif opcao == "4":
                break

                # Caso a opção não seja válida
            else:
                print("Opção inválida. Tente novamente.")

                # Função responsável por remover um livro da lista


    def remover_livro():
        id_remover = int(input("Digite o ID do livro que deseja remover: "))
        encontrado = False
        for livro in lista_livro:
            if livro["id"] == id_remover:
                lista_livro.remove(livro)
                print(f"Livro com o ID {id_remover} removido com sucesso.")
                encontrado = True
                break
        if not encontrado:
            print("Livro não encontrado.")

            # Menu principal do programa (laço principal)


    while True:
        print("\nMenu principal")

        print("1. Cadastrar livro")
        print("2. Consultar livro")
        print("3. Remover livro")
        print("4. Sair")

        # Recebe a opção escolhida pelo usuário
        opcao = input("Escolha uma opção: ")

        # Executa a função de cadastro e atualiza o ID global
        if opcao == "1":
            id_global += 1
            cadastrar_livro(id_global)

            # Chama a função de consulta de livros
        elif opcao == "2":
            consultar_livro()

            # Chama a função para remover um livro
        elif opcao == "3":
            remover_livro()

            # Encerra o programa
        elif opcao == "4":
            print("Encerrando o programa... Obrigado por usar a nossa livraria!")
            break

            # Caso o usuário digite uma opção inválida
        else:
            print("Opção inválida. Tente novamente.")