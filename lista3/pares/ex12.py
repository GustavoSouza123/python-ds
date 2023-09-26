num = int(input("Entre com um número para mostrar sua tabuada: "))

print(f"\nTabuada de {num}:", end="\n\n")
for i in range(1, 11):
    print(f"{num} x {i} = {num*i}")