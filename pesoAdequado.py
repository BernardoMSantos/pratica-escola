print("Descubra qual é seu peso ideal:")
print("")

sexo = input("Qual é seu gênero?(M/F)")
altura = float(input("Digite sua altura:"))

if sexo == "M":
    pesoIdeal = (72.7 * altura) - 58
else:
    pesoIdeal = (62.1 * altura) - 44.7

print(f"Seu peso ideal é {pesoIdeal}")