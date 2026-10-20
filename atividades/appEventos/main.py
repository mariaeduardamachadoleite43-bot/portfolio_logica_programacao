from tarefas import tarefas
import os
os.system ('cls')

while True:
    print("\n --- Lista de Tarefas")
    print("1 - Adicionar Tarefas")
    print("2 -Listar Tarefas")
    print("3 - Sair")
    
    opcao = int(input('digite a opção desejada:'))
    
    if(opcao == 1):
        print('opção para adicioar uma tarefa')
    elif(opcao == 2):
        print('opção para listar tarefas')
    elif(opcao == 3):
        print('programa encerrado') 
        break
    else:
        print('número inválido')   