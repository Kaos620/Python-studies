class Task:
    def __init__(self, name, hours, done=False):
        self.name = name
        self.hours = hours
        self.done = done


def menu():
    print("\n [1] Inserir nova tarefa na lista")
    print("\n [2] Marcar Tarefa como feita")
    print("\n [3] Remover uma tarefa da lista")
    print("\n [4] Imprimir lista de tarefas pendentes")
    print("\n [5] Imprimir lista de tarefas finalizadas")
    print("\n [6] Sair")


def start():
    print("[1] Entrar")
    print("[2] Sair")


def tasksToDo():
    print("[a] Imprimir em ordem alfabetica")
    print("[b] Imprimir em Ordem Crescente pro Propriedade de Esforco")
    print("[c] Imprimir em Ordem Decrescente pro Propriedade de Esforco")


def tasksDone():
    print("[a] Imprimir em ordem alfabetica")
    print("[b] Imprimir em Ordem Crescente pro Propriedade de Esforco")
    print("[c] Imprimir em Ordem Decrescente pro Propriedade de Esforco")

tasks_list = []
index = 0

start()
optionStart = int(input("\nEscolha a Acao: \n"))
while optionStart == 1:
    menu()
    option = int(input("\nEscolha a Acao: \n"))
    if option == 1:
        limit = int(input("\nQuantas Tarefas voce gostaria de adicionar? \n"))
        counter = 0
        while counter < limit:
            counter += 1
            name = str(input("Digite o nome da tarefa: \n"))
            hours = int(input("Quantas horas foram usadas na tarefa? \n"))
            new_task = Task(name, hours)
            tasks_list.append(new_task)
        for i, task in enumerate(tasks_list):
            print(
                f"\n Lista numero {i+1}\nO nome da tarefa e {task.name} \n Voce gastou {task.hours} horas nela. \n Ela foi concluida? {task.done} \n")
    elif option == 2:
        task_index = int(
            input("Qual tarefa voce gostaria de marcar como concluida? \n"))
        tasks_list[task_index - 1].done = True
        print(
            f"Tarefa '{tasks_list[task_index - 1].name}' marcada como concluida!")
    elif option == 3:
        task_index = int(input("Qual tarefa voce gostaria de remover? \n"))
        removed_task = tasks_list.pop(task_index - 1)
        print(f"\n A task {removed_task} foi removida com sucesso")
    elif option == 4:
        tasksToDo()
        toDo = input("\nEm que formato voce gostaria de ver a lista?")
        if toDo == 'a':
            sorted_tasks = sorted(tasks_list, key=lambda task: task.name)
        elif toDo == 'b':
            sorted_tasks = sorted(tasks_list, key=lambda task: task.hours)
        elif toDo == 'c':
            sorted_tasks = sorted(tasks_list, key=lambda task: task.hours, reverse=True)
        else:
            break
        for i, task in enumerate(sorted_tasks):
            print(f"\nLista numero {i+1}\n O nome da tarefa e {task.name} \n Voce gastou {task.hours} horas nela.")
    elif option == 5:
        tasksDone()
        taskDone = input("Em que formato voce gostaria de ver a lista?")
        if taskDone == 'a':
            sorted_tasks = sorted(tasks_list, key=lambda task: task.name)
        elif taskDone == 'b':
            sorted_tasks = sorted(tasks_list, key=lambda task: task.hours)
        elif taskDone == 'c':
            sorted_tasks = sorted(tasks_list, key=lambda task: task.hours, reverse=True)
        else:
            break
        for i, task in enumerate(sorted_tasks):
            print(f"\nLista numero {i+1}\n O nome da tarefa e {task.name} \n Voce gastou {task.hours} horas nela.")
    else:
        break
