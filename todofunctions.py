default_filepath = "todos.txt"


def read_todos(filepath=default_filepath):
    with open(filepath, "r") as file_local:
        todos_local = file_local.readlines()
    return todos_local


def write_todos(todos_arg, filepath=default_filepath):
    with open(filepath, "w") as file_local:
        file_local.writelines(todos_arg)
