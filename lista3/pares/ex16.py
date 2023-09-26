ultimo = 0
atual = 1
resultado = ultimo + atual

print(ultimo, atual, end=" ")

while resultado <= 500:
    print(resultado, end=" ")
    aux = ultimo
    ultimo = atual
    atual += aux
    resultado = ultimo + atual