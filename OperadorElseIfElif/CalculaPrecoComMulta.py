#entradas
peso_de_peixes = float(input("Informe o peso dos peixes: "))
#processamento
if peso_de_peixes > 50:
    multa = (peso_de_peixes - 50) * 4.00
    excesso = 'excesso' 
    print("Você deverá pagar R$ {0:.2f}".format(multa))
else:
    multa = 0
    excesso = 0
    print("Multas: {0}".format(multa))
    print("Excesso: {0}".format(excesso))

