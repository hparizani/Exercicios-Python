#variáveis
valor_hora = 10.00
valor_hora_excedente = 20.00
e = 0
#entradas
c = int(input("Informe o código: "))
n = float(input("Informe a quantidade de horas trabalhadas: "))
valor_hora = 10.00
valor_hora_excedente = 20.00
#processamento
if n > 50:
    e = (n - 50) * valor_hora_excedente #20.00
    salario = 50 * valor_hora #10.00
    print("Seu salário total é: R$ {0:.2f}".format(salario + e))
    print("Salário excedente: R$ {0}".format(e))
else:
    salario = n * valor_hora
    print("Seu salário total é: R$ {0:.2f}".format(salario))
    print("Salário excedente: R$ {0}".format(e))