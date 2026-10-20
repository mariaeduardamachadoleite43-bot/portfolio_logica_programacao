import os
os.system("cls || clear")

print("Digite o valor da compra")
valor = float(input())
print("Digite o valor do desconto")
desconto = float(input())
print("Digite o valor do frete")
frete = float(input())
desconto = valor * (desconto/ 100)
total = valor - desconto + frete 
print("Subtotal :", valor)
print("Desconto :", desconto)
print("Frete :", frete)
print("Total final :", total)