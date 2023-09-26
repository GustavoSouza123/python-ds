senha_salva = "123456"
senha_digitada = ""
repeticoes = 0

while senha_salva != senha_digitada:
    repeticoes += 1
    senha_digitada = input(f"Sua senha ({repeticoes}x): ")

print(f"{repeticoes} repetições")
print("Este laço (while) pode ter repetições infinitas")