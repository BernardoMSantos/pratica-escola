print("--Cadastre seu produto--")
produto = input("Qual é o seu produto?\n -")
i = True
while i == True:
    print("Categorias dos produtos: \n [1]Limpeza \n [2]Alimentação \n [3]Bebidas \n [4]Utilidades ao lar \n [5]Têxtil \n [6]Açougue")
    categoria = int(input("Digite qual categoria o seu produto se classifica: "))

    if categoria == 1:
        print(f"O produto {produto} ficará na categoria: Limpeza")
        i = False
    elif categoria == 2:
        print(f"O produto {produto} ficará na categoria: Alimentação")
        i = False
    elif categoria == 3:
        print(f"O produto {produto} ficará na categoria: Bebidas")
        i = False
    elif categoria == 4:
        print(f"O produto {produto} ficará na categoria: Utilidades")
        i = False
    elif categoria == 5:
        print(f"O produto {produto} ficará na categoria: Têxtil")
        i = False
    elif categoria == 6:
        print(f"O produto {produto} ficará na categoria: Açougue")
        i = False
    else:
        print("Porfavor diga uma uma das categorias mostradas")
        i = True