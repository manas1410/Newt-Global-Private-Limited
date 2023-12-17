while True:
    user_Action = input("Type add, show, edit, complete or exit: ")
    user_Action = user_Action.strip()

    if user_Action.startswith("add"):
        todo = user_Action[4:]+"\n"

        with open("todos.txt", "r") as file:
            todos = file.readlines()

        todos.append(todo)

        with open("todos.txt", 'w') as file:
            file.writelines(todos)

    elif user_Action.startswith("show"):
        with open("todos.txt", "r") as file:
            todos = file.readlines()

        for index, item in enumerate(todos):
            row = f"{index + 1}-{item.strip('\n')}"
            print(row)

    elif user_Action.startswith("edit"):
        try:
            number = int(user_Action[5:])

            with open("todos.txt", "r") as file:
                todos = file.readlines()

            existing_todo = todos[number - 1]
            new_todo = input("Enter new todo: ")
            todos[number - 1] = new_todo + "\n"

            with open("todos.txt", 'w') as file:
                file.writelines(todos)
        except ValueError:
            print("Your command is not valid.")
            continue

    elif user_Action.startswith("complete"):
        try:
            number = int(user_Action[9:])

            with open("todos.txt", "r") as file:
                todos = file.readlines()

            index = number - 1
            todo_to_remove = todos[index].strip('\n')
            todos.pop(index)

            with open("todos.txt", 'w') as file:
                file.writelines(todos)

            message = f"Todo {todo_to_remove} was removed from the list."
            print(message)
        except IndexError:
            print("There is no iteam with that number.")
            continue

    elif user_Action.startswith("exit"):
        break
    else:
        print("Command is not valid")

print("Bye!")




