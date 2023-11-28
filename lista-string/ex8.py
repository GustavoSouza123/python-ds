string = input("Entre com uma palavra ou frase para ver se é um palíndromo: ")

str = string.replace(" ", "")
strAoContrario = ""

for i in range(len(str)):
    strAoContrario += str[len(str)-i-1]

palindromo = "não "
if strAoContrario == str:
    palindromo = ""

print(f"A string \"{string}\" {palindromo}é um palíndromo")