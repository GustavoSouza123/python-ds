nome = input("Entre com o seu nome: ")
nome = nome.upper()

for i in range(len(nome)):
    print(nome[len(nome)-i-1])