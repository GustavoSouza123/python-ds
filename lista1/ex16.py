tamanho_metros2 = int(input("Entre com o tamanho em metros quadrados da área a ser pintada: "))
quant_latas = (tamanho_metros2 / 3) / 18
preco_total = quant_latas * 80
print(f"Quantidade de latas de tinta a serem compradas: {quant_latas:.1f}")
print(f"Preço total: R$ {preco_total:.2f}")