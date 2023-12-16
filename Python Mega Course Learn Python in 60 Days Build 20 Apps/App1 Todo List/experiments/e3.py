todos = []

while True:
    user_Action = input("Type add or show, or exit: ")
    user_Action = user_Action.strip()

    match user_Action:
        case 'add':
            todo = input("Enter a todo: ")
            todos.append(todo)
        case 'show' | 'display':
            for item in todos:
                item = item.title()
                print(item)
        case 'exit':
            break
        case _:
            print("Hey, you entered an unknown command")

print("Bye!")




