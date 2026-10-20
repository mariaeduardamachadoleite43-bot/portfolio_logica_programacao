import os
os.system("cls || clear")

# Lista – despensa flexível (pode ser modificada) 
frutas_lista = ["maçã", "banana", "laranja"] 

# Tupla – despensa fixa (não pode ser modificada) 
temperos_tupla = ("sal", "pimenta", "açúcar") 

# String – despensa de caracteres 
palavra_string = "PYTHON" 


for frutas in frutas_lista :
    print(frutas)
    
for frutas in temperos_tupla :
    print(frutas)
    
for letras in palavra_string :
    print(letras)
    
    
    
modificavel = [1, 2, 3, 4, 5]
print(modificavel) # [1, 2, 3, 4, 5]
modificavel[0] = 0 #1º posição vira 0
print(modificavel) # [0, 2, 3, 4, 5]

tupla = (1, 2, 3, 4, 5) 
print(tupla) # (1, 2, 3, 4, 5) 
# tupla[0] = 0 
print(tupla) # erro, pois não pode ser alterado

string = 'PYTHON'
print(string[0]) #