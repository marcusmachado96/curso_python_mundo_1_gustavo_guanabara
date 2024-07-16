from random import choice

num = [1, 2, 3, 4, 5]
nume = (choice(num))
print('Vou pensar em um numero de 1 até 5, tente acertar')
escnum = int(input('Qual numero você escolhe: '))

while nume != escnum:
    escnum = int(input('Não é esse, escolha outro número: '))
else:
    print('Parabéns, você acertou !\n'
          '_______________________')
