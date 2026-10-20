import os
os.system('cls||clear')

idade = int(input("Digite a idade:"))
if (idade <16):
    print("Não pode entrar")
elif (idade <=17):
    print("Pode etrar com o responsável")
elif (idade >=18):
    print("Entrada liberada")