str1 = input("Entre com a primeira string: ")
str2 = input("Entre com a segunda string: ")

print(f"Tamanho de \"{str1}\": {len(str1)} caracteres")
print(f"Tamanho de \"{str2}\": {len(str2)} caracteres")

if(len(str1) != len(str2)):
    print("As duas string são de tamanhos diferentes")
else:
    print("As duas string são de tamanhos iguais")

if(str1 != str2):
    print("As duas strings possuem conteúdo diferente")
else:
    print("As duas strings possuem conteúdo igual")