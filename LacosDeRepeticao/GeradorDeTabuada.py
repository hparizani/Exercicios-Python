# Entrada
num = int(input("Tabuada: informe um número de 1 a 10: "))
while num < 1 or num > 10:
    num = int(input("Erro: Informe um número entre 1 e 10: "))
# Processamento / Saída
for i in range(1, 11):
    print("{0}X{1} = {2}".format(num, i, (num * i)))