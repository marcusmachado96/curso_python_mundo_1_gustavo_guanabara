from math import radians, sin, cos, tan
ang = float(input("Digiteo ângulo que você deseja: "))
seno = sin(radians(ang))
print("O ângulo de {} tem o SENO de {:.2f}".format(ang, seno))
cosseno = cos(radians(ang))
print("O ângulo de {} tem o COSSENO de {:.2f}".format(ang, cosseno))
tang = tan(radians(ang))
print("O ângulo de {} tem a TANGENTE de {:.2f}".format(ang, tang))
