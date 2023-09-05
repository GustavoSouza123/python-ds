saque = float(input("Entre com o valor do saque: "))

if saque < 10 or saque > 600:
    print("O valor mínimo do saque é de R$ 10, e o máximo é de R$ 600")
else:
    notas100 = int(saque / 100)
    saque = saque % 100
    notas50 = int(saque / 50)
    saque = saque % 50
    notas10 = int(saque / 10)
    saque = saque % 10
    notas5 = int(saque / 5)
    saque = saque % 5
    notas1 = int(saque)
    print(f"{notas100} notas de 100")
    print(f"{notas50} notas de 50")
    print(f"{notas10} notas de 10")
    print(f"{notas5} notas de 5")
    print(f"{notas1} notas de 1")