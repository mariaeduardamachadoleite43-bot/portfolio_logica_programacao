import os
os.system("cls || clear")

nome = input('Digite seu nome:')
produto = input('Digite o nome do produto:')
quantidade = int(input('Digite a quantidade:'))
valor = float (input('Digite o valor:'))
print('Você recebeu um cumpom de 18%')
pagamento = input('Digite a forma do pagamento ')
total = quantidade * valor
total =(total* 0.9)
print('Resuma a compra')
print(f'Cliente:{nome}')
print(f'Produto: {produto}')
print(f'quantidade: {quantidade}')
print(f'Preç unitario: R$ {valor}')
print(f'forma de pagamento:{pagamento}')
print(f'total a pagar: R$ {total}')
os.system('cls||clear')