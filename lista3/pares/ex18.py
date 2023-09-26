n = int(input("Entre com o número de números que deseja entrar: "))

menor = 0
maior = 0
soma = 0

for i in range(n):
    num = int(input(f"Entre com o {i+1}º número: "))
    if i == 0:
        menor = num
        maior = num
    else:
        if num < menor:
            menor = num
        if num > maior:
            maior = num
    soma += num

print(f"\nMenor valor: {menor}")
print(f"Maior valor: {maior}")
print(f"Soma dos valores: {soma}")