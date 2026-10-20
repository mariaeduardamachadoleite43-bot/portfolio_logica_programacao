import os
os.system ('cls')

n = 0
contador = 0
acumulador = 0

while (n != -1):
    n = float(input('Digite um numero: '))
    contador = contador = 1
    acumulador = acumulador + n
    if (n == 0):
         print('programa encerrado')
         break

contador = 1
acumulador = 1
m = acumulador + contador
print(f'a soma é {m}')