FILEPATH = "todos.txt"

def get_todos(filepath=FILEPATH):
    """ Open, reads and returns the content of to-do file"""
    with open(filepath, 'r') as file_local:
        todos_local = file_local.readlines()
    return todos_local


def write_todos(todos_arg, filepath=FILEPATH):
    with open(filepath, 'w') as file:
        file.writelines(todos_arg)


if __name__ == "__main__":
    print("hello from Functions MODULE!")