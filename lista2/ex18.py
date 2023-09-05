data = str(input("Entre com uma data no formato dd/mm/aaaa: "))

try:
    if data[:2].isdigit() and data[3:5].isdigit() and data[6:] and data[2] == "/" and data[5] == "/":
        print(f"`{data}` é uma data válida")
    else:
        print(f"`{data}` não é uma data válida")
except:
    print(f"`{data}` não é uma data válida")