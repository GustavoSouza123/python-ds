while True:
    num = int(input("\nEntre com um número para ver se ele é primo: "))
    if num < 2:
        print("O número deve ser maior ou igual a 2")
    else:
        break

if num == 2:
    print("O número 2 é primo")
else:
    divisores = ""
    for i in range(2, num):
        if num % i == 0:
            divisores += str(i) + ", "
        if i == num-1:
            if divisores != "":
                print(f"O número {num} não é primo")
                print(f"Seus divisores são: {divisores[:len(divisores)-2]}")
            else:
                print(f"O número {num} é primo")