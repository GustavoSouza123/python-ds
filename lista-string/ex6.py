data = input("Entre com sua data de nascimento: ")
dataArr = data.split("/")

mes = ""

match int(dataArr[1]):
    case 1:
        mes = "Janeiro"
    case 2:
        mes = "Fevereiro"
    case 3:
        mes = "Março"
    case 4:
        mes = "Abril"
    case 5:
        mes = "Maio"
    case 6:
        mes = "Junho"
    case 7:
        mes = "Julho"
    case 8:
        mes = "Agosto"
    case 9:
        mes = "Setembro"
    case 10:
        mes = "Outubro"
    case 10:
        mes = "Novembro"
    case 12:
        mes = "Dezembro"

print(f"Você nasceu em {dataArr[0]} de {mes} de {dataArr[2]}")