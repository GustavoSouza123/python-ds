usuario = input("Entre com um nome de usuário: ")

while True:
    senha = input("Entre com sua senha: ")
    if senha == usuario:
        print("A senha não deve ser igual ao nome do usuário")
    else:
        break

print(f"\nUsuário: {usuario}\nSenha: {senha}")