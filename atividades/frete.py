import os
os.system ("cls || clear")

peso = float (input("Digite o peso do pacote"))

if (peso > 10) :
    print("Frete expresso")
elif (peso> 2) :
    print("Frete econômico")
else:
    tipoFrete = str(input("Digite o tipo do frete "))