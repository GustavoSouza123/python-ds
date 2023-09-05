ano = int(input("Entre com um ano para ver se é bissexto: "))

if ano % 4 == 0:
    print(f"{ano} é bissexto!")
else:
    print(f"{ano} não é bissexto!")