import os 
os.system('cls')

# notas = [7.0, 8.5, 6.0, 9.0, 5.5]

# quantidadeValores = len(notas)
# indicePrimeiroValor = notas.index(7)
# ultimoIndice = len(notas)- 1

# i = 0
# while i < 5: # ao em vez de colar 5 pode colocar len(notas) / len(notas) é o tamanho da lista
#     print(notas[i])
#     i += 1

#desafio
notas = [7.0, 8.5, 6.0, 9.0, 5.5]
l = len(notas) 
print(f'existem {l} valores nessa lista.')
maior = 0 
for a in notas:
    if a > maior:
        maior = a
print(f'o maior valor dessa lista é {maior}')

ac = 0
for i in notas:
    ac += i
print(f'a soma de todos os valores dessa lista é {ac}')