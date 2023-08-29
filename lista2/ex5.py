n1 = float(input("Entre com a primeira nota: "))
n2 = float(input("Entre com a segunda nota: "))
media = (n1 + n2) / 2

if media == 10:
    print("Aprovado com distinção")
elif media >= 7:
    print("Aprovado")
else:
    print("Reprovado")