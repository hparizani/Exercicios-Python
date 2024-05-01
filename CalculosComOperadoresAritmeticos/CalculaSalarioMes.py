# Entradas
valor_por_hora = float(input("Qual valor você ganha por hora? "))
horas_trabalhadas = int(input("Quantas horas você trabalhou nesse mês: "))
# Processamento
salario_por_mes = valor_por_hora * horas_trabalhadas
# Saída
print("Neste mês você vai receber R$ {0:.2f}".format(salario_por_mes))