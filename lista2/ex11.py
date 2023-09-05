salarioAntigo = float(input("Entre com o seu salário: "))

if salarioAntigo <= 280:
    reajuste = 0.20
elif salarioAntigo > 280 and salarioAntigo <= 700:
    reajuste = 0.15
elif salarioAntigo > 700 and salarioAntigo <= 1500:
    reajuste = 0.10
else:
    reajuste = 0.05

salarioNovo = salarioAntigo + (salarioAntigo * reajuste)

print(f"Salário antes do reajuste: {salarioAntigo:.2f}")
print(f"Percentual de aumento aplicado: {reajuste*100:.0f}%")
print(f"Valor do aumento: {salarioNovo-salarioAntigo:.2f}")
print(f"Salário após o aumento: {salarioNovo:.2f}")