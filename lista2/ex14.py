nota1 = float(input("Entre com a primeira nota: "))
nota2 = float(input("Entre com a segunda nota: "))
media = (nota1 + nota2) / 2

if media >= 9 and media <= 10:
    conceito = "A"
elif media >= 7.5 and media < 9:
    conceito = "B"
elif media >= 6 and media < 7.5:
    conceito = "C"
elif media >= 4 and media < 6:
    conceito = "D"
elif media >= 0 and media < 4:
    conceito = "E"
else:
    conceito = "Erro"

if conceito == "A" or conceito == "B" or conceito == "C":
    mensagem = "Aprovado"
elif conceito == "D" or conceito == "E":
    mensagem = "Reprovado"
else:
    mensagem = "Erro"

print(f"Nota 1: {nota1}")
print(f"Nota 2: {nota2}")
print(f"Média: {media}")
print(f"Conceito: {conceito}")
print(f"{mensagem}!")