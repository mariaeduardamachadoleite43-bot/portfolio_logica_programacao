import os
os.system("cls || clear")

contador = 0
acumulador = 0

valores = [52.50, 22.90, 34.0, 48.90, 50.0] 

for numeros in valores: #for , variável e a lista
    print("Lista de valores:", (numeros))
    contador = contador + 1
    acumulador = acumulador + numeros

acumulador + 1
print(f'Quantidade de valores listados: {contador}') 
print(f'A soma dos valores é de: {acumulador}')
    
