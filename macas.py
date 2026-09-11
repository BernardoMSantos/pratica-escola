print("BEM VINDO A LOJA DE MAÇÃS:")
print("Uma maçã vale 0.30, mas se comprar uma dúzia(12) cada maçã sai por 0.25")
print("")

macasCompradas = int(input("Quantas maçãs você deseja comprar?"))

if macasCompradas >= 12:
    valorPagar = macasCompradas * 0.25
else:
    valorPagar = macasCompradas * 0.30

print(f"Você vai levar {macasCompradas} maçãs, o valor que tem que pagar é {valorPagar}.")