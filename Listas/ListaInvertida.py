#variáveis
vetor = []
#entradas
for n in range(0, 10):
    num = int(input("Digite um valor: "))
    vetor.append(num)
#processamento
vetor.reverse() #inverte a lista
for n in vetor:
    print(n)