str = input("Entre com uma frase qualquer: ")

espacos = 0
vogais = 0

for i in range(len(str)):
    if str[i] == " ":
        espacos += 1
    if str[i] == "a" or str[i] == "e" or str[i] == "i" or str[i] == "o" or str[i] == "u":
        vogais += 1

print(f"A frase \"{str}\" tem {espacos} espacos e {vogais} vogais")