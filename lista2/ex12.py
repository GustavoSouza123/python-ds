salarioHora = float(input("Entre com o seu salário por hora: "))
horasTrabalhadas = int(input("Entre com a quantidade de horas trabalhadas no mês: "))

salarioBruto = salarioHora * horasTrabalhadas

if salarioBruto <= 1903.98:
    percImpostoRenda = 0
elif salarioBruto <= 2836.65:
    percImpostoRenda = 0.075
elif salarioBruto <= 3751.05:
    percImpostoRenda = 0.15
elif salarioBruto <= 4664.68:
    percImpostoRenda = 0.15
else:
    percImpostoRenda = 0.275

impostoRenda = salarioBruto * percImpostoRenda
sindicato = salarioBruto * 3 / 100
fgts = salarioBruto * 8 / 100

salarioLiquido = salarioBruto - impostoRenda - sindicato

print(f"Salário bruto: R$ {salarioBruto:.2f}")
print(f"IR: ({(percImpostoRenda*100):.1f}%): R$ {impostoRenda:.2f}")
print(f"FGTS (8%): R$ {fgts:.2f}")
print(f"Sindicato (3%): R$ {sindicato:.2f}")
print(f"Total de descontos: R$ {(impostoRenda+sindicato):.2f}")
print(f"Salário líquido: R$ {salarioLiquido:.2f}")