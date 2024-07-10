print("Estimativa de quantidade de tinta em litros para pintar paredes")
lar = float(input("Digite a largura da parede: "))
alt = float(input("Digite a altura da parede: "))
area = lar * alt

# Um litro de tinta pinta em média 9m² e custa aproximadamente R$ 12,60
tinta = area / 9
valor = 12.6 * tinta

print("Para pintar uma área de {:.2f}m² você vai precisar de {:.2f}l de tinta. O custo da tinta será aproximadamente R$ {:.2f} ".format(area, tinta, valor))


