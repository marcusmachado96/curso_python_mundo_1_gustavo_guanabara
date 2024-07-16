vel = int(input('Qual a velocidade do carro: '))
if vel > 80:
    print('O carro foi multado')
    mult = (vel - 80)*7
    print('O valor da multa será: R$ {}'.format(mult))
else:
    print('___________________')

