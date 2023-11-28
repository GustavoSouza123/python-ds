def corrigir_telefone(telefone):
    if "-" in telefone:
        telefone = telefone.replace("-", "")
    if len(telefone) == 7:
        telefone = "3" + telefone
    return telefone

telefone = input("Digite o número de telefone: ")
telefone_corrigido = corrigir_telefone(telefone)

print("Telefone corrigido sem formatação:", telefone_corrigido)
print("Telefone corrigido com formatação:", telefone_corrigido[:4] + "-" + telefone_corrigido[4:])