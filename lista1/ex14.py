# testar
peso = int(input("Entre com o peso de peixes: "))
excesso = 0
if peso > 50: excesso = peso - 50
multa = 4 * excesso
print(f"O peso de peixes é {peso} kg. O excesso foi {excesso} kg, logo o valor da multa é de R$ {multa}")