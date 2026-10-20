import os 
os.system('cls')

def ler_vetor():
    nums = [] #Cria uma lista vazia chamada 'nums'
    n = int(input("Quantos números?")) #armazena em 'n' quantos números existirão na lista
    for i in range(n): #for vai rodar a quantidade de números que a lista terá
        valor = int(input("Digite um números:")) #Armazena em 'valor' o número digitado
        nums.append(valor) #adiciona o número dito pelo usuário na lista nums
    return nums

def exibir_vetor(nums):
    print("vetor:", nums) #mostra a lista nums
    
def somar_vetor(nums):
    soma= 0
    for v in nums:
        soma += v
    return soma
    
def calcular_media_vetor(nums):
    soma = somar_vetor(nums)
    media = soma / len(nums)
    return media

def encontrar_maior_valor(nums):
    maior = nums[0]
    for v in nums:
        if v > maior:
            maior = v
    return maior

#Teste de leitura de dados
vn = ler_vetor()

#Teste de exibição do vetor
ev = exibir_vetor(vn)

#Teste de soma do vetor
sv = somar_vetor(vn)
print(sv)

cmv = calcular_media_vetor(vn)
print(cmv)

emv = encontrar_maior_valor(vn)
print(emv)
