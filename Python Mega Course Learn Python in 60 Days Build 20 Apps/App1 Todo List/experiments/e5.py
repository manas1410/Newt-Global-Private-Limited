todos = []

while True:
    user_Action = input("Type add, show, edit, complete or exit: ")
    user_Action = user_Action.strip()

    match user_Action:
        case 'add':
            todo = input("Enter a todo: ")
            todos.append(todo)
        case 'show':
            for index, item in enumerate(todos):
                row = f"{index + 1}-{item}"
                print(row)
            print("Hello", index, item)
            print("Length is:",len(todos))
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



#2
for i, j in enumerate("Hello"):
    print(i, j)

a = enumerate(['a','b','c'])
print(list(a)) #[(0, 'a'), (1, 'b'), (2, 'c')]