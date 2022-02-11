loginAdministrador = "robocop"
senhaAdministrador = "001"

tentativas = 5

while tentativas != 0:
    login = input("Insira seu login: ")
    senha = input("insira sua senha: ")

    tentativas = tentativas - 1
    if login == loginAdministrador and senha == senhaAdministrador:
        print("Usuário autorizado")
        exit()
    else:
        print("Usuário não autorizado")

