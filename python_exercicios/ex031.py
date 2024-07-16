vpass = int(input('Escolha o conforto da poltrona\n'
              'Digite 1 - Normal // R$ 50\n'
              'Digite 2 - Plus // R$ 85\n'
              ))
if vpass == 1:
    vpass = 50
else:
    vpass = 85

dis = float(input('Qual a distância da sua viagem em Km: '))
if dis < 200:
    valpass1 = (dis * 0.50)+vpass
    print('O valor da passagem será de R$ {}'.format(valpass1))
else:
    valpass2 = (dis * 0.45)+vpass
    print('O valor da passagem será de R$ {}'.format(valpass2))
