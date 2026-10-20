import os 
os.system('cls')

contador = 0

tabuada = int(input('Bem vindo!\nAqui você pode descobrir a tabuada que quiser(1-10)\nDigite o número desejado:\n'))
for i in range(1, 11):
    contador += 1
    print(f'{tabuada} x {contador} = {contador*tabuada}')