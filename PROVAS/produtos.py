print("Bem-vindo a nossa loja! - Vendemos pães cariocas e leite em caixa:")
pao = float(input("Quantos cariocas -0,25- você quer: "))
leite = float(input("Quantos caixas de leite -2,5- você quer: "))
 
valorPao = pao * 0.25
valorLeite = leite * 2.50

if pao > 0 and leite  > 0:
    print(f"Você terá que pagar um total de {valorPao + valorLeite}, {valorPao} de pão e {valorLeite} de leite.")
else:
    if pao <= 0 and leite > 0:
        print(f"Você terá que pagar um total de {valorLeite}.")
    elif leite <= 0 and pao > 0:
        print(f"Você terá que pagar um total de {valorPao}.")
    else:
        print("Obrigado volte sempre!")