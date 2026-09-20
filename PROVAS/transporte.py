def voltarInicio():
    escolha = input("Você quer voltar ao início?[S/N] ")
    if escolha == "n" or escolha == "N":
        i = False
        return i
    else:
        i = True
        return i



i = True
while i == True:
    print("=" *  21)
    print("SISTEMA DE TRANSPORTE")
    print("=" * 21)

    escolha = input("[1]Classificar Passageiro \n[2]Verificar Desconto \n[3]Sair\n>")
    if escolha == "1":
        idade = float(input("Digite a idade do passageiro: "))
        if idade < 6:
            print("Você é uma criança")
            voltar = voltarInicio()
            if voltar == False:
                i = False
        elif idade >= 6 and idade <= 17:
            print("Você é um adolecente")
            voltar = voltarInicio()
            if voltar == False:
                i = False
        elif idade > 17 and idade <= 59:
            print("Você é um adulto")
            voltar = voltarInicio()
            if voltar == False:
                i = False
        else: # Para pessoas de 60 anos para cima
            print("Você é um idoso")
            voltar = voltarInicio()
            if voltar == False:
                i = False

    elif escolha == "2":
        idade = float(input("Digite a idade do passageiro: "))
        if idade < 6:
            print("A passagem será gratuita")
            i = False
        elif idade >= 6 and idade <= 17:
            passagem = 300 - (300 * 0.2)
            print(f"A passagem fica por R$300, mas com desconto de 20%, ficando por {passagem}")
            i = False
        elif idade >= 18 and idade < 60:
            print("A passagem fica por R$250")
            i = False
        else:
            passagem = 200 - (200 * 0.5)
            print(f"A passagem fica por R$200, mas com desconto de 50%, ficando por {passagem}")
            i = False

    elif escolha == "3":
        print("Você tem certeza?\n...")
        # Volta ao início
        voltar = voltarInicio()
        if voltar == False:
            i = False

    else:
        print("Opção inválida")
        voltar = voltarInicio()
        if voltar == False:
            i = False
print(f"Programa encerrado. Obrigado por utilizar o SISTEMA DE TRANSPORTE!")    