#Entradas
num1 = int(input("Informe o primerio número: "))
num2 = int(input("Informe o segundo número: "))
num3 = int(input("Informe o terceiro número: "))
num4 = int(input("Informe o quarto número: "))
#Processamentos
q1 = num1 * num1
q2 = num2 * num2
q3 = num3 * num3
q4 = num4 * num4
if q3 >= 1000:
    print("O quadrado de {0} é: {1}".format(num3,q3))
else:
    print("O quadrado de {0} é: {1}".format(num1,q1))
    print("O quadrado de {0} é: {1}".format(num2,q2))
    print("O quadrado de {0} é: {1}".format(num3,q3))
    print("O quadrado de {0} é: {1}".format(num4,q4))
    