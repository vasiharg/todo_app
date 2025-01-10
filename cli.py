# from functions import get_todos, write_todos
import functions
import time

now = time.strftime("%b %d, %Y %H:%M:%S")
print("It is, ", now)
while True:
    user_action = input("Type add, edit, show, complete or exit:")
    user_action = user_action.strip()

    if user_action.startswith('add'):
        todo = user_action[4:]

        todos = functions.get_todos()

        todos.append(todo + '\n')

        functions.write_todos(todos, 'todos.txt')

    elif user_action.startswith('show'):
        todos = functions.get_todos()

        # list comprehension - useful feature to work with a list
        # new_todos = [item.strip('\n') for item in todos]

        for index, item in enumerate(todos):
            item = item.strip('\n')
            row = f"{index + 1}.{item}"
            print(row)

    elif user_action.startswith('edit'):
        try:
            number = int(user_action[4:])
            number = number - 1

            todos = functions.get_todos()

            new_todo = input('Enter new todo: ')
            todos[number] = new_todo + '\n'

            functions.write_todos(todos, 'todos.txt')
        except ValueError:
            print('Your command is not valid!')
            continue
    elif user_action.startswith('complete'):
        try:
            number = int(user_action[9:])
            todos = functions.get_todos()

            index = number - 1
            todo_to_remove = todos[index].strip('\n')
            todos.pop(index)

            functions.write_todos(todos, 'todos.txt')
            message = f"To do {todo_to_remove} was complete"
            print(message)
        except IndexError:
            print('Index of the task you have entered, is not in your List')
            continue
    elif user_action.startswith('exit'):
        break
    else:
        print('This command is not valid!')
print('Bye!!!Bye')