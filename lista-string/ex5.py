nome = input("Entre com o seu nome: ")

for i in range(len(nome)):
    print(nome[:len(nome)-i])