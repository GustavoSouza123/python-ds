soma = 0
for i in range(1, 6):
    num = int(input(f"Entre com o {i}º número: "))
    soma += num

print(f"\nSoma dos números: {soma}")
print(f"Média dos números: {(soma/5):.1f}")