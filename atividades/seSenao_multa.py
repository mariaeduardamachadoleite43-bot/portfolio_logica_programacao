import os
os.system("cls || clear")

velocidade = 95
multa = 0

if (velocidade > 80):
    multa = (velocidade - 80) * 5.50
    print("Você ganhou uma multa de R$", multa)
else:
    print("Sua velocidade está dentrodo limite!")
print("Fim do programa")