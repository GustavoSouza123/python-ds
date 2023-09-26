while True:
    n = int(input("\nEntre com o número de notas que deseja entrar para calcular a média delas: "))
    if n < 2:
        print("O número de notas deve ser maior ou igual a 2")
    else:
        break

print()

media = 0
i = 0
while i < n:
    nota = float(input(f"Entre com a {i+1}º nota: "))
    if nota < 0 or nota > 10:
        print("A nota deve ser um número entre 0 e 10\n")
        continue
    media += nota
    i += 1

media /= n
print(f"\nA média das {n} notas é: {media}")