from random import sample

def embaralhar(str):
    str = sample(str, len(str))
    newStr = ""
    return newStr.join(str)

while True:
    string = input("Entre com uma string para embaralhar (0 para sair): ")
    if string == "0":
        break
    print(embaralhar(string))