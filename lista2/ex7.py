n1 = int(input("Entre com o primeiro número: "))
n2 = int(input("Entre com o segunda número: "))
n3 = int(input("Entre com o terceira número: "))

maior = 0
menor = 0

if n1 > n2 and n1 > n3:
    maior = n1
    if n2 < n3:
        menor = n2
    else:
        menor = n3
elif n2 > n1 and n2 > n3:
    maior = n2
    if n1 < n3:
        menor = n1
    else:
        menor = n3
else:
    maior = n3
    if n1 < n2:
        menor = n1
    else:
        menor = n2

print(f"Maior: {maior}\nMenor: {menor}")