nota1 = float(input("Entre com a primeira nota: "))
nota2 = float(input("Entre com a segunda nota: "))
nota3 = float(input("Entre com a terceira nota: "))
media = (nota1 + nota2 + nota3) / 3

if media == 10:
    print(f"Aprovado com distinção")
elif media >= 7:
    print(f"Aprovado (média: {media:.2f})")
elif media < 7:
    print(f"Reprovado (média: {media:.2f})")