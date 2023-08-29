prod1 = float(input("Entre com o preço do primeiro produto: "))
prod2 = float(input("Entre com o preço do segundo produto: "))
prod3 = float(input("Entre com o preço do terceiro produto: "))

if prod1 < prod2 and prod1 < prod3:
    print("Compre o primeiro produto")
elif prod2 < prod1 and prod2 < prod3:
    print("Compre o segundo produto")
else:
    print("Compre o terceiro produto")