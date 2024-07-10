nome = input ("Digite seu nome \n")
print ("Prazer em te conhecer",(nome))

# Exercicio pessoal // detector de eleitor valido com confirmação de voto

idade = int(input("Quantos anos você tem ? \n"))

if idade >= 16:
    confirmar = 0
    while confirmar != 1:
        voto = int(input("Digite seu voto\n"))
        confirmar = int(input(f"Seu voto foi: {voto} ?\n  1 - Confirmar / 2 - Cancelar\n"))
    else:
        print(f"Obrigado por votar")
else:
    print("Desculpa você não pode votar")
