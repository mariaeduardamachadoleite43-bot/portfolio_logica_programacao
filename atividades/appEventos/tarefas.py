import os
os.system ('cls')

tarefas = []

def adicionar_tarefas(nome):
    tarefas.append(nome)
    print('tarefa adicionada com sucesso!')
    return tarefas