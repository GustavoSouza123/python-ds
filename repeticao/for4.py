""" for (continue, break, else) """

for i in range(6):
    if i == 2:
        print("i = 2, pulando...")
        continue
    if i == 5:
        print("i = 5, else não executará")
        break
    for j in range(1, 3):
        print(i, j)
else:
    print("For completo com sucesso!")