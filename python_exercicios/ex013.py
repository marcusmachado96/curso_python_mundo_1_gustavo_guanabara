sal = float(input("Qual o salario do funcionario ? R$ "))
porc = int(input("Qual a porcentagem de aumento do salario ? "))
aum = (sal * (porc / 100))
aum_cheio = sal + aum
print("Com {}% de aumento o valor do salario atualizado é R$ {:.2f}, o valor do aumento foi de R$ {:.2f}".format(porc,aum_cheio,aum))