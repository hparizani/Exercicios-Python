# Construa um algoritmo que leia 10 valores inteiros e positivos e:
# a) Encontre o maior valor
# b) Encontre o menor valor
# c) Calcule a média dos números lidos

# Variáveis
maior = -999
menor = 999
soma = 0

# Entradas / processamento
for i in range(1, 11):
    num = int(input("Informe o número {0}/10 positivo: ".format(i)))
    if num > 0:
        if num > maior:
            maior = num
        if num < menor:
            menor = num
        soma = soma + num
    else:
        valor = int(input("Informe um valor: "))
media = soma / i

# saídas
print("O maior número é: {0}".format(maior))
print("O menor número é: {0}".format(menor))
print("A média dos números é: {0}".format(media))