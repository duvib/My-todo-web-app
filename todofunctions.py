FILEPATH = "C:/Users/duvar/PycharmProjects/pythonProject/.venv/To-do list/todos.txt"

def read_todos(filepath = FILEPATH):
    """Read file and make list. """
    with open(filepath, "r") as file_local:
        todos_local = file_local.readlines()
    return todos_local


def write_todos(todos_arg, filepath = FILEPATH):
    """Write new todos into file"""
    with open(filepath, "w") as file_local:
        file_local.writelines(todos_arg)
