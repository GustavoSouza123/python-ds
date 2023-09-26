pares = 0
impares = 0

for i in range(1, 11):
    num = int(input(f"Entre com o {i}º número inteiro: "))
    if num % 2 == 0:
        pares += 1
    else:
        impares += 1

print(f"\n{pares} números pares")
print(f"{impares} números ímpares")