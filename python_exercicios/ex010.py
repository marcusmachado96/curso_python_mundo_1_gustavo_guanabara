din = float(input("Quantos reais você tem ? R$ "))

dol = din / 5.41
eu = din / 5.85
lib = din / 6.93
bit = din / 315275.875

print("Você pode comprar {:.2f} dolares\n"
        "Você pode comprar {:.2f} euros\n"
        "Você pode comprar {:.2f} libras\n"
        "Você pode comprar {:.6f} bitcoins\n".format(dol,eu,lib,bit))


