import os
os.system("cls || clear")

compra = float(input("Digite o valor da compra: R$ "))
if (compra >= 300):
  print("voê ganhou um desconto de 15%!")
  desconto = 0.15
elif (compra >= 200):
  print("você ganhou um desconto de 12%!")  
  desconto = 0.12
else:
    desconto = 0.10
    
modulo = (compra * desconto)
total = compra - modulo
print(f"resumo da sua compra\n seu desconto foi de {modulo}\n o total da sua compra foi {total}")