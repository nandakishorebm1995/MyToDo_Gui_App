FILEPATH = 'todos.txt'


def get_todos(filepath=FILEPATH):
    # doc-strings are function specific information that is prompted when searched for that function. It is usually
    # written in the first line of a function-snippet. It is written within triple quotes.
    """Opens, reads and returns the content from the file
    stated in the arguments."""
    with open(filepath, 'r') as readfile:
        todos_local = readfile.readlines()
    return todos_local


# print(help(get_todos))


def write_todo_file(todos_arg, filepath=FILEPATH):
    """Opens and write the to-do items in the text file."""
    with open(filepath, 'w') as writefile:
        writefile.writelines(todos_arg)


if __name__ == "__main__":
    print('Hi... a message from main_functions!')
