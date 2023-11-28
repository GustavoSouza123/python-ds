import random

def escolher_palavra():
    with open("palavras.txt", "r") as arquivo:
        palavras = arquivo.readlines()
    return random.choice(palavras).strip()

def embaralhar_palavra(palavra):
    return ''.join(random.sample(palavra, len(palavra)))

def jogo_embaralhado():
    palavra_secreta = escolher_palavra()
    palavra_embaralhada = embaralhar_palavra(palavra_secreta)
    tentativas = 6

    print("Bem-vindo ao Jogo da Palavra Embaralhada!")
    print(f"Adivinhe a palavra embaralhada: {palavra_embaralhada}")

    while tentativas > 0:
        tentativa = input("Sua tentativa: ").lower()

        if tentativa == palavra_secreta:
            print(f"Parabéns! Você acertou a palavra '{palavra_secreta}'.")
            break
        else:
            tentativas -= 1
            print(f"Você errou! Você tem mais {tentativas} tentativas.")

    if tentativas == 0:
        print(f"Suas tentativas acabaram. A palavra era '{palavra_secreta}'.")

# iniciando o jogo
jogo_embaralhado()