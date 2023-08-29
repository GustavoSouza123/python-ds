nome = input("Entre com o seu primeiro nome: ")
cont = 0

for letra in nome:
    if letra.isdigit() == True or letra is None or letra == " ":
        break
    else:
        cont += 1

if cont == 0:
    print("Nome inválido")
elif cont <= 4:
    print("Seu nome é curto")
elif cont <= 6:
    print("Seu nome é normal")
else:
    print("Seu nome é muito grande")