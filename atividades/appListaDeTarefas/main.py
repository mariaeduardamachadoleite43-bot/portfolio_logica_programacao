import os
import time
from tarefas import lista_tarefas, criar_tarefa, listar_tarefa, apagar_tarefa

os.system("cls")

def executar_menu():
    while True:
        time.sleep(2)
        print('\n --------Menu Principal')
        print('1. Criar Tarefa')
        print('2. Listar Tarefa(s)')
        print('3. Atualizar Tarefa')
        print('4. Apagar Tarefa')
        print('5. Sair')
        
        opcao = int(input("Escolha uma opção:"))
        
        if (opcao == 5):
            print('Programa encerrado.')
            break
        elif (opcao == 1):
            nome = str(input('Digite o nome da tarefa'))
            criar_tarefa(nome)
        elif (opcao == 2):
            listar_tarefa()
        elif (opcao == 3):
            numero_tarefa = int(input('Digite o número da tarefa que será atualizada como "concluída "'))
            apagar_tarefa(numero_tarefa)
            
    
        
executar_menu()
        