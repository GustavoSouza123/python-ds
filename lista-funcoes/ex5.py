def converterHorario(hrs, mins):
    global str
    str = 'A'
    if hrs > 12:
        hrs -= 12
        str = 'P'
    return f"{hrs}:{mins}"

def imprimirHorario(horario):
    global str
    str = str+'.M.'
    print(f'{horario} {str}')

while True:
    hrs = int(input('Entre com as horas: '))
    mins = int(input('Entre com os minutos: '))
    if hrs == 0 and mins == 0:
        break
    horario = converterHorario(hrs, mins)
    imprimirHorario(horario)