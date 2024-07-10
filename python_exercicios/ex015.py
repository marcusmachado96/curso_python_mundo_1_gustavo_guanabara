print("Aluguel de carros")
d_alug = int(input("Quantos dias o carro foi alugado ?  "))
km_rod = float(input("Quantos Km rodados ?  "))
val = (d_alug * 70)+(km_rod * 3)
print("{} dias alugados e {}Km percorridos\n"
      "Total a pagar é R$ {}".format(d_alug,km_rod,val))