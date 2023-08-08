import math

print()
tamanho_metros2 = int(input("Entre com o tamanho em metros quadrados da área a ser pintada: "))
litros_tinta = int(tamanho_metros2 / 6)
quant_latas = math.ceil(litros_tinta / 18)
quant_galoes = math.ceil(litros_tinta / 3.6)
quant_mist = f"{int(litros_tinta // 18)} latas, {math.ceil(litros_tinta % 18 / 3.6)} galões"

preco_total_latas = quant_latas * 80
preco_total_galoes = quant_galoes * 25
preco_mist = (int(litros_tinta // 18)) * 80 + (math.ceil(litros_tinta % 18 / 3.6)) * 25

print()
print(f"Para pintar {tamanho_metros2} m2, serão necessários {litros_tinta} litros de tinta")
print()
print(f"O preço total é: ")
print(f"> Comprando apenas latas de 18 litros ({quant_latas} latas): R$ {preco_total_latas:.2f}")
print(f"> Comprando apenas galões de 3,6 litros ({quant_galoes} galões): R$ {preco_total_galoes:.2f}")
print(f"> Misturando latas e galões para evitar o desperdício de tinta ({quant_mist}): R$ {preco_mist}")