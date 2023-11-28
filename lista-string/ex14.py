def leet_speak(texto):
    leet_dict = {'a': '4', 'e': '3', 'l': '1', 'o': '0', 't': '7'}
    texto_leet = ''.join(leet_dict[letra] if letra in leet_dict else letra for letra in texto.lower())
    return texto_leet

texto_original = input("Digite um texto: ")
texto_leet = leet_speak(texto_original)

print("Texto em Leet Speak:", texto_leet)