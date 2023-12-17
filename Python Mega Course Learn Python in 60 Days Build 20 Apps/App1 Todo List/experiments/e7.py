while True:
    # Get user input and strip space chars from it
    user_Action = input("Type add, show, edit, complete or exit: ")
    user_Action = user_Action.strip()

    match user_Action:
        case 'add':
            todo = input("Enter a todo: ") + "\n"

            file = open("todos.txt","r")
            todos = file.readlines()
            file.close()

            todos.append(todo)

            # Write todos in todos.txt
            file = open("../todos.txt", 'w')
            file.writelines(todos)
            file.close()

        case 'show':
            file = open("../todos.txt", "r")
            todos = file.readlines()
            file.close()

            new_todos = [item.strip('\n') for item in todos]

            for index, item in enumerate(new_todos):
                row = f"{index + 1}-{item}"
                print(row)

        case "edit":
            number = int(input("Number of the todo to edit: "))
            existing_todo = todos[number - 1]
            new_todo = input("Enter new todo: ")
            todos[number - 1] = new_todo
        case "complete":
            number = int(input("Number of the todo to complete: "))
            todos.pop(number - 1)
        case 'exit':
            break
        case _:
            print("Hey, you entered an unknown command")

print("Bye!")




