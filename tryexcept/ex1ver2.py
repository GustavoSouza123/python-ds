num_str = input("Entre com um número inteiro: ")

try:
    num_int = int(num_str)
    if num_int % 2 == 0:
        print("Este número é par")
    else:
        print("Este número é ímpar")
except:
    print("Isso não é um número")