loginAdministrador = "robocop"
senhaAdministrador = "001"
senhas = ["facebook: 123", "google: 456"]

tentativas = 5

while tentativas != 0:
    login = input("Insira seu login: ")
    senha = input("insira sua senha: ")

    tentativas = tentativas - 1
    if login == loginAdministrador and senha == senhaAdministrador:
        print("Usuário autorizado")
        print("Opções: ")
        print("1 - Listar senhas: ")
        print("2 - Editar senha: ")
        print("3 - Excluir senha: ")
        opcao = int(input("Insira sua opção: "))

        if opcao == 1:
            print(senhas)

    else:
        print("Usuário não autorizado")
        print("Tente novamente.")

