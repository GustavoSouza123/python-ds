n1 = float(input("Entre com o primeiro número: "))
n2 = float(input("Entre com o segundo número: "))
operacao = str(input("Entre com a operação que deseja (somar, subtrair, multiplicar, dividir): "))

if operacao == "somar":
    res = n1 + n2
elif operacao == "subtrair":
    res = n1 - n2
elif operacao == "multiplicar":
    res = n1 * n2
elif operacao == "dividir":
    res = n1 / n2
else:
    operacao = "erro"

if operacao == "erro":
    print("Erro na operação")
else:
    if res == 0:
        print(f"{res} é nulo")
    else:
        if res %  2 == 0:
            parimpar = "par"
        else:
            parimpar = "ímpar"

        if res >= 0:
            posneg = "positivo"
        else:
            posneg = "negativo"

        if res != int(res):
            intdec = "decimal"
        else:
            intdec = "inteiro"
        
        print(f"{res} é {parimpar}, {posneg} e {intdec}")