# Entradas
altura = float(input("Informe a sua altura: "))
sexo = input("Informe seu sexo: 'm' para masculino ou 'f' para feminino: ")
# Processamento
if sexo.lower() == 'm':
    peso_ideal = (72.7 * altura) - 58
elif sexo.lower() == 'f':
    peso_ideal = (62.1 * altura) - 44.7
else:
    peso_ideal = 0
    print("Sexo não reconhecido.")
# Saída
print("Seu peso ideal é {0:.2f}".format(peso_ideal))