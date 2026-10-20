import os
os.system ('cls')

#. Desenhem o vetor: Desenhem o vetor em seu papel ou editor, deixando espaço logo abaixo para anotações.
vetor = [40, 20,50,10]

#Comparação 1: Olhem para os dois primeiros elementos: 40 e 20. 40 > 20? Sim. Troquem-nos
vetor = [20,40,50,10]

#Comparação 2: Agora, olhem para o segundo e terceiro elementos do novo vetor: 40 e 50. 40 > 50? Não. Não façam nada.
vetor = [20,40,50,10]

#3. Comparação 3: Olhem para o terceiro e quarto elementos: 50 e 10. 50 > 10? Sim. Troquem-nos
vetor = [20,40,10,50]
#Finalizado a 1° passada

#2° passada
#1° comparação. 20>40? Não, então mantenha
vetor = [20,40,10,50]

#2comparação. 40>10? sim, então troque
vetor = [20,10,40,50]

#3º Comparação. 40>50? Não, então mantenha
vetor = [20,10,40,50]

#3º Passada
# 1º Comparação. 20>10? Sim, então troque
vetor = [10,20,40,50]

# 2º Comparação. 20>40? Não, então mantenha
vetor =[10,20,40,50]

# 3º Comparação. 40>50? Não, então mantenha
vetor = [10,20,40,50]