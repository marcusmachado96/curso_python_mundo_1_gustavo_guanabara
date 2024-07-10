valor = float(input("Qual o valor do produto? R$ "))
porc = int(input("Qual a porcentagem do desconto ? "))
desc = ((valor * (porc / 100)))
val_final = valor - desc

print("O valor final do produto será R$ {:.2f}, você esta economizando R$ {:.2f}".format(val_final,desc))

