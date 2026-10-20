import os
os.system("cls || clear")

idade = int(input("Digite a sua idade:\n"))
if(idade>= 16) :
    print("Você pode votar!")
    if(idade >= 18) :
        print("Voto obrigatório")
    else:
         print("Voto facultativo")
else:
    print("Você ainda não pode votar")
    print("Faltam", 16 - idade,"anos")
    