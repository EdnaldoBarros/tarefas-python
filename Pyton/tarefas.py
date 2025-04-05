# Lista vazia para armazenar as tarefas
tarefas = []

# Loop principal do programa
while True:
    # Exibe o menu
    print("\n--- MENU ---")
    print("1. Adicionar nova tarefa")
    print("2. Listar todas as tarefas")
    print("3. Remover uma tarefa")
    print("4. Sair")

    # Recebe a escolha do usuário
    escolha = input("Escolha uma opção (1-4): ")

    # Opção 1: Adicionar tarefa
    if escolha == "1":
        nova_tarefa = input("Digite a nova tarefa: ")
        tarefas.append(nova_tarefa)
        print("Tarefa adicionada com sucesso!")

    # Opção 2: Listar tarefas
    elif escolha == "2":
        if not tarefas:
            print("Nenhuma tarefa cadastrada.")
        else:
            print("\n--- LISTA DE TAREFAS ---")
            for i, tarefa in enumerate(tarefas, start=1):
                print(f"{i}. {tarefa}")

    # Opção 3: Remover tarefa
    elif escolha == "3":
        if not tarefas:
            print("Não há tarefas para remover.")
        else:
            for i, tarefa in enumerate(tarefas, start=1):
                print(f"{i}. {tarefa}")
            try:
                num = int(input("Digite o número da tarefa a remover: "))
                if 1 <= num <= len(tarefas):
                    removida = tarefas.pop(num - 1)
                    print(f"Tarefa '{removida}' removida com sucesso!")
                else:
                    print("Número inválido.")
            except ValueError:
                print("Por favor, digite um número válido.")

    # Opção 4: Sair do programa
    elif escolha == "4":
        print("Saindo do programa. Até logo!")
        break

    # Opção inválida
    else:
        print("Opção inválida. Tente novamente.")
