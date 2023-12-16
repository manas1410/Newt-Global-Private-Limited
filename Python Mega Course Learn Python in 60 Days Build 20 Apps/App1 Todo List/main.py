user_promt = "Enter a todo: "

todos = []

while True:
    todo = input(user_promt)
    #todos.append() - It will give Error
    print(todo.capitalize())
    todos.append(todo)
    print(todos)
