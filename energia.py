energia = float(input("Quantos KWh você gastou esse mês? "))
lugar = float(input("Digite: \n[1] para residêncial, \n[2] para indústria, \n[3] para comércio"))

if lugar == 1:
    if energia <= 500:
        energiaPagar = energia * 0.40
    elif energia > 500:
        energiaPagar = energia * 0.65
if lugar == 2:
    if energia <= 1000:
        energiaPagar = energia * 0.55
    elif energia > 1000:
        energiaPagar = energia * 0.60
if lugar == 3:
    if energia <= 5000:
        energiaPagar = energia * 0.55
    elif energia > 5000:
        energiaPagar = energia * 0.60

print(f"Você gastou {energia} na sua {lugar}, você terá que pagar {energiaPagar}")