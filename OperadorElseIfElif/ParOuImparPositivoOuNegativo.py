# Entrada
num = int(input("Informe um número: "))
# Processamento
if num % 2 == 0:
    if num > 0:
        print("O número {0} é par e positivo".format(num))
    else:
        print("O número {0} é par e negativo".format(num))
else:
    if num > 0:
        print("O número {0} é ímpar e positivo".format(num))
    else:
        print("O número {0} é ímpar e negativo".format(num))