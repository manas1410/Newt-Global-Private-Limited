def get_todos(filepath):
    filepath = "todos1.txt"
    with open(filepath, "r") as file:
        todos_local = file.readlines()
    return filepath


def write_todos(filepath,todos_arg):
    with open(filepath, 'w') as file:
        file.writelines(todos_arg)


while True:
    user_Action = input("Type add, show, edit, complete or exit: ")
    user_Action = user_Action.strip()

    if user_Action.startswith("add"):
        todo = user_Action[4:] + "\n"

        todos = get_todos("todos.txt")

        todos.append(todo)

        write_todos("todos.txt", todos)

    elif user_Action.startswith("show"):
        todos = get_todos("todos.txt")

        for index, item in enumerate(todos):
            row = f"{index + 1}-{item.strip('\n')}"
            print(row)

    elif user_Action.startswith("edit"):
        try:
            number = int(user_Action[5:])

            todos = get_todos("todos.txt")

            existing_todo = todos[number - 1]
            new_todo = input("Enter new todo: ")
            todos[number - 1] = new_todo + "\n"

            write_todos("todos.txt", todos)
        except ValueError:
            print("Your command is not valid.")
            continue

    elif user_Action.startswith("complete"):
        try:
            number = int(user_Action[9:])

            todos = get_todos("todos.txt")

            index = number - 1
            todo_to_remove = todos[index].strip('\n')
            todos.pop(index)

            write_todos("todos.txt", todos)

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