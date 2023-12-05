from random import randint

def lancarDados():
    return randint(2, 12)

jogadas = 0
ponto = 0
while True:
    string = input('Entre com qualquer valor para jogar os dados: ')
    if string:
        jogadas += 1
        num = lancarDados()
        print(f'Número: {num}')
        if jogadas == 1:
            if num == 7 or num == 11:
                print('Você ganhou!')
                break
            elif num == 2 or num == 3 or num == 12:
                print('Você perdeu')
                break
            else:
                print('Este é o seu ponto. Continue jogando os dados até tirar este número novamente')
                ponto = num
        else:
            if num == ponto:
                print('Você ganhou!')
                break
            elif num == 7:
                print('Você perdeu!')
                break