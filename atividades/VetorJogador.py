import os 
os.system('cls')

# Pontuações do jogador
pontuacao = [80, 100, 60, 120] #lista unidimencional pos nao tem comprimento

# Inicializando as variáveis para coletar estatísticas
soma = 0
maior = pontuacao [0] #80
menor = pontuacao [0] #80

# # 1º Rodada
# soma = soma + pontuacao[0]
# #2º Rodada
# soma = soma + pontuacao[1]
# #3º Rodada
# soma = soma + pontuacao[2]
# #4º Rodada
# soma = soma + pontuacao[3]

# if (pontuacao[0] > maior):
#     maior = pontuacao[0]
# if (pontuacao[1] > maior):
#     maior = pontuacao[1]
# if (pontuacao[2] > maior):
#     maior = pontuacao[2]
# if (pontuacao[3] > maior):
#    maior = pontuacao [3]
# print(maior)
 
for i in range(4):
    soma = soma + pontuacao [i]
    if (pontuacao[i] > maior):
            maior = pontuacao[i]
     
print(soma) 
print(f'o maior é {maior}')

for a in range(4):
    if (pontuacao[a] < menor):
        menor = pontuacao[a]
print(f'o menor é {menor}')
    