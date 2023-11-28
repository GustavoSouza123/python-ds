cpf = input("Entre com o seu CPF: ")

try:
    cpfArr = cpf.split(".")
    finalCpfArr = cpfArr[2].split("-")

    if len(cpf) == 14 and cpfArr[0].isdigit() and cpfArr[1].isdigit() and finalCpfArr[0].isdigit() and finalCpfArr[1].isdigit():
        print(f"O CPF {cpf} é válido")
    else:
        print(f"O CPF {cpf} não é válido")
except:
    print(f"O CPF {cpf} não é válido")