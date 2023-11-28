import random

def escolher_palavra():
    with open("palavras.txt", "r") as arquivo:
        palavras = arquivo.readlines()
    return random.choice(palavras).strip()

def mostrar_palavra(palavra, letras_corretas):
    resultado = ""
    for letra in palavra:
        if letra in letras_corretas:
            resultado += letra + " "
        else:
            resultado += "_ "
    return resultado.strip()

def jogo_forca():
    palavra_secreta = escolher_palavra()
    letras_corretas = []
    tentativas = 0

    print("Bem-vindo ao Jogo da Forca!")
    print("Adivinhe a palavra:")
    print(mostrar_palavra(palavra_secreta, letras_corretas)+"\n")

    while tentativas < 6:
        letra = input("Digite uma letra: ").lower()

        if letra in letras_corretas:
            print(f"A letra '{letra}' já foi escolhida. Tente de novo!")
        elif letra in palavra_secreta:
            letras_corretas.append(letra)
            print(f"A palavra é: {mostrar_palavra(palavra_secreta, letras_corretas)}")
        else:
            tentativas += 1
            print(f"Você errou pela {tentativas}ª vez. Tente de novo!")

        if set(letras_corretas) == set(palavra_secreta):
            print("Parabéns! Você adivinhou a palavra!")
            break

    if tentativas == 6:
        print(f"Você foi enforcado! A palavra era '{palavra_secreta}'.")

# iniciando o jogo
jogo_forca()