print()

while True:
    num = int(input("Entre com um número inteiro para calcular seu fatorial (caso queira sair, digite 0): "))

    if num == 0:
        break
    elif num < 0 or num >= 16:
        print("O número deve ser inteiro, positivo e menor que 16\n")
        continue
    
    entrada = num
    res = num
    num -= 1
    while num > 1:
        res *= num
        num -= 1

    print(f"O fatorial de {entrada} é {res}\n")

print(f"\nFim do loop!")