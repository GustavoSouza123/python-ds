sal_hora = float(input("Entre com quanto você ganha por hora: "))
horas_trabalhadas = int(input("Entre com o número de horas trabalhadas por mês: "))

salario_bruto = sal_hora * horas_trabalhadas
imposto_ir = salario_bruto * 11/100
imposto_inss = salario_bruto * 8/100
imposto_sindicato = salario_bruto * 5/100
salario_liquido = sal_hora * horas_trabalhadas - imposto_ir - imposto_inss - imposto_sindicato
print(f"+ Salário Bruto: R$ {salario_bruto}")
print(f"- IR (11%): R$ {imposto_ir}")
print(f"- INSS (8%): R$ {imposto_inss}")
print(f"- Sindicato (5%): R$ {imposto_sindicato}")
print(f"= Salário Líquido: R$ {salario_liquido}")