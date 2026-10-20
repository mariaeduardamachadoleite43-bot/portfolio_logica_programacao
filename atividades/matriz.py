import os
os.system("cls")

# matriz = [1, 0, 1, 0] #lista normal
# print(matriz [0]) #1
# print(matriz[1]) #0
# print(matriz[2]) #1
# print(matriz[3]) #0


matriz = [[1,0,1,0], 
          [0,0,1,1], 
          [1,1,1,1]]

# print(matriz[0][0])
# print(matriz[0][1])
# print(matriz[0][2])
# print(matriz[0][3])
# print(matriz[1][0])
# print(matriz[1][1])
# print(matriz[1][2])
# print(matriz[1][3])
# print(matriz[2][0])
# print(matriz[2][1])
# print(matriz[2][2])
# print(matriz[2][3])

for linha in range(3):
    for coluna in range(4):
        print(matriz[linha][coluna])
        
 #Outra forma de fazer
# for i in matriz:
#     for a in i:
#      print(a)

