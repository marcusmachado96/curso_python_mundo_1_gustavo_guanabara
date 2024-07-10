#Exercicio pessoal, utilizando repetição

numtab = int(input("Digite um numero para ver sua tabuada de 1 a 10: "))
tab10 = 0
print("_____________")
while tab10 < 10:
    tab10 = tab10 + 1
    res = numtab * tab10
    print ("{:2} x {:2} = {}".format(numtab,tab10,res))
print("_____________")
