lado1 = float(input("Entre com o primeiro lado de um triângulo: "))
lado2 = float(input("Entre com o segundo lado de um triângulo: "))
lado3 = float(input("Entre com o terceiro lado de um triângulo: "))

if lado1+lado2 > lado3 or lado1+lado3 > lado2 or lado2+lado3 > lado1:
    triangulo = "sim"
    if lado1 == lado2 and lado1 == lado3:
        tipoTriangulo = "equilátero"
    elif lado1 == lado2 or lado1 == lado3 or lado2 == lado3:
        tipoTriangulo = "isósceles"
    else:
        tipoTriangulo = "escaleno"
else:
    triangulo = "não"

print(f"Lados: lado 1 = {lado1}, lado 2 = {lado2}, lado 3 = {lado3}")
print(f"É um triângulo: {triangulo}")
if triangulo == "sim": print(f"Tipo do triângulo: {tipoTriangulo}")