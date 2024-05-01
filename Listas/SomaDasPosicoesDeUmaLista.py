# variáveis
vetor = []
for i in range(0, 20):
    num = int(input("Informe {0}/20 valor para o vetor: ".format(i+1)))
    vetor.append(num)
print("A soma do vetor é {0}".format(sum(vetor)))