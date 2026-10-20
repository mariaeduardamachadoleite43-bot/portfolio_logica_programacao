import os
os.system("cls || clear")

nomes_dos_alunos = ["Duda", "Beth", "Cássia", "Vitória", "Bianca", "Fernanda", "Mirella", "Michelle"] #primeiro conta 0
contador = 0

for alunos in nomes_dos_alunos: #for , variável e a lista
    print("Aluno(a)", (alunos))
    contador = contador + 1
     
    
print(f'Na sala tem {contador}') #contar quantas pessoas tem na sala
