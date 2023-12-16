todos = []

while True:
    user_Action = input("Type add, show, edit or exit: ")
    user_Action = user_Action.strip()

    match user_Action:
        case 'add':
            todo = input("Enter a todo: ")
            todos.append(todo)
        case 'show' | 'display':
            for item in todos:
                print(item)
        case "edit":
            number = int(input("Number of the todio to edit: "))
            existing_todo = todos[number - 1]
            new_todo = input("Enter new todo: ")
            todos[number - 1] = new_todo
        case 'exit':
            break
        case _:
            print("Hey, you entered an unknown command")

print("Bye!")




