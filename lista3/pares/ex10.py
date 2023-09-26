num1 = int(input("Entre com o primeiro número inteiro: "))
num2 = int(input("Entre com o segundo número inteiro: "))

print()

if num1 == num2:
    print("Os números são iguais")
elif num1 < num2:
    num1 += 1
    while num1 < num2:
        if num1 == num2-1:
            print(num1)
            break
        print(num1, end=", ")
        num1 += 1
else:
    num1 -= 1
    while num1 > num2:
        if num1 == num2+1:
            print(num1)
            break
        print(num1, end=", ")
        num1 -= 1