codigo = int(input("Informe o código: "))
vetor = []
if codigo == 0:
    print("Fim do programa.")
elif codigo == 1:
    for n in range(0, 5):
        num = float(input("Informe o número real {0}/5 do vetor: ".format(n + 1)))
        vetor.append(num)
    for n in vetor:
        print(n)
elif codigo == 2:
    for n in range(0, 5):
        num = float(input("Informe o número real {0}/5 do vetor: ".format(n + 1)))
        vetor.append(num)
    vetor.reverse() # inverte a lista
    for n in vetor:
        print(n)



    