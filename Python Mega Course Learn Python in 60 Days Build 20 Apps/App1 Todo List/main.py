todos = []

while True:
    user_Action = input("Type add or show, or exit: ")
    user_Action = user_Action.strip()

    match user_Action:
        case 'add':
            todo = input("Enter a todo: ")
            todos.append(todo)
        case 'show':
            for item in todos:
                print(item)
        case 'exit':
            break


print("Bye!")




