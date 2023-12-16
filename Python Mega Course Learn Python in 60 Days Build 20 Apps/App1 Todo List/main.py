todos = []

while True:
    user_Action = input("Type add or show, or exit:")

    match user_Action:
        case 'add':
            todo = input("Enter a todo: ")
            todos.append(todo)
        case 'show':
            print(todos)
        case 'exit':
            break

print("Bye!")




