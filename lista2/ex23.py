num = float(input("Entre com um número para ver se ele é inteiro ou decimal: "))

if num != int(num):
    print(f"{num} é decimal")
else:
    print(f"{num} é inteiro")