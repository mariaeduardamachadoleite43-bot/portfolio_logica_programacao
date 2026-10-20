import os
os.system ('cls')

matriz = [[1,2,3,], 
          [4,5,6,], 
          [7,8,9]]

for linha in range(3):
    for coluna in range(3):
        print(matriz[linha][coluna])
        
acumulador = 0


for coluna in range(0,2):

    acumulador = acumulador + matriz[0][linha]

print(f'A soma da linha 1 é {acumulador}')


for coluna in range(0,2):

    acumulador = acumulador + matriz[1][linha]

print(f'A soma da linha 1 é {acumulador}')


for coluna in range(0,2):

    acumulador = acumulador + matriz[2][linha]

print(f'A soma da linha 1 é {acumulador}')








        

