nome = input("Nome: ")
sobrenome = input("Sobrenome: ")
ano_atual = int(input("Ano atual: "))
ano_nasc = int(input("Seu ano de nascimento: "))
idade_atual = ano_atual - ano_nasc
idade_2050 = 2050 - ano_nasc

print()

# usando o método format
print("Meu nome é {} {}".format(nome, sobrenome))
print("O ano atual é {} e meu ano de nascimento é {}".format(ano_atual, ano_nasc))
print("Logo, minha idade é {}, e em 2050 terei {} anos".format(idade_atual, idade_2050))

print()

# usando f-strings
str = f"Meu nome é {nome} {sobrenome}\nO ano atual é {ano_atual} e meu ano de nascimento é {ano_nasc}\nLogo, minha idade é {idade_atual}, e em 2050 terei {idade_2050} anos"
print(str)