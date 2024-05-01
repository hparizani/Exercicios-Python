# entradas
nome = input("Informe o nome de usuário: ")
senha = input("Informe a sua senha: ")
# processamento
while nome == senha:
    print("Nome de usuário não pode ser igual a senha.")
    nome = input("Informe o nome de usuário: ")
    senha = input("Informe a sua senha: ")