import math

a = float(input("Entre com o valor de a: "))

if a == 0:
    print("A equação não é do segundo grau")
else:
    b = float(input("Entre com o valor de b: "))
    c = float(input("Entre com o valor de c: "))

    delta = (b * b) - 4 * a * c
    if delta < 0:
        print("A equação não possui raizes reais")
    elif delta == 0:
        x = (-b + math.sqrt(delta)) / 2 * a
        print(f"A equação possui apenas uma raiz real:\nx = {x:.2f}")
    else:
        x1 = (-b + math.sqrt(delta)) / 2 * a
        x2 = (-b - math.sqrt(delta)) / 2 * a
        print(f"A equação possui duas raizes reais:\nx1 = {x1:.2f}, x2 = {x2:.2f}")