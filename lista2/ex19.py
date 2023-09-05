num = int(input("Entre com um número inteiro menor que 1000: "))

if num < 1000:
    unidades = int((num % 100) % 10)
    dezenas = int(((num-unidades) % 100) / 10)
    centenas = int(num / 100)

    centenasPlural = "s" if centenas > 1 else ""
    dezenasPlural = "s" if dezenas > 1 else ""
    unidadesPlural = "s" if unidades > 1 else ""

    print(f"{num} = {centenas} centena{centenasPlural}, {dezenas} dezena{dezenasPlural} e {unidades} unidade{unidadesPlural}")
else:
    print("O número deve ser menor que 1000")