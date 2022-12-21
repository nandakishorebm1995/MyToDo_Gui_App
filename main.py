import PySimpleGUI as sg
import main_functions
import time
import os

if not os.path.exists("todos.txt"):
    with open("todos.txt", "w") as file:
        pass

sg.theme("BluePurple")

clock = sg.Text(time.strftime("%b %d, %Y %H:%M:%S"), key="clock")
label = sg.Text("Type in your To-Do:", font="Helvetica 13 bold")
input_box = sg.InputText(tooltip="Enter todo", key="To-Do")
add_button = sg.Button(size=1, image_source="add1.png", button_color="lightblue2",
                       mouseover_colors="white", border_width=0, tooltip="Add ToDo", key="Add")
list_box = sg.Listbox(values=main_functions.get_todos(), key="todos", enable_events=True, size=(45, 10))
edit_button = sg.Button("Edit")
complete_button = sg.Button(image_source="complete1.png", button_color="lightblue2",
                            mouseover_colors="white", border_width=0, tooltip="Complete ToDo", key="Complete")
finish_button = sg.Button(size=10, image_source="complete_all1.png", button_color="lightblue2",
                          mouseover_colors="white", border_width=0, tooltip="Complete all ToDos", key="Complete all")
exit_button = sg.Button("Exit", border_width=2, button_color="red", font="bold")

window = sg.Window("My To-Do App",
                   layout=[[clock],
                           [label],
                           [input_box, add_button],
                           [list_box], [edit_button, complete_button, finish_button, sg.Push(), exit_button]],
                   font=("Helvetica", 13))

while True:
    event, values = window.read(timeout=10)
    window["clock"].update(value=time.strftime("%b %d, %Y %H:%M:%S"))
    # print(event)
    # print(values)
    # event is the label of the button pushed
    # values are the input given by the user during that event.
    match event:
        case "Add":
            todos = main_functions.get_todos()
            user_input = values["To-Do"]
            if len(user_input) == 0:
                continue
            todo = user_input + '\n'
            todos.append(todo)
            main_functions.write_todo_file(todos)
            window["todos"].update(values=todos)
            window["To-Do"].update(value=[])

        case "Edit":
            try:
                edit_todo = values["todos"][0]
                todos = main_functions.get_todos()
                edit_idx = todos.index(edit_todo)
                edited_todo = values["To-Do"]
                todos[edit_idx] = edited_todo
                main_functions.write_todo_file(todos)
                window["todos"].update(values=todos)
                window["To-Do"].update(value=[])
            except IndexError:
                sg.popup("Please select an item first to edit it.", title="First select",
                         font=("Helvetica", 10))

        case "Complete":
            try:
                todo_complete = values["todos"][0]
                todos = main_functions.get_todos()
                complete_idx = todos.index(todo_complete)
                todos.pop(complete_idx)
                main_functions.write_todo_file(todos)
                window["todos"].update(values=todos)
                window["To-Do"].update(value=[])
            except IndexError:
                sg.popup("There are no items in your list. Please select an item first.", title="First add",
                         font=("Helvetica", 10))

        case "Complete all":
            todos = main_functions.get_todos()
            if len(todos) == 0:
                sg.popup("There are no items in your list. Please add an item first.", title="First add",
                         font=("Helvetica", 10))
            else:
                answer = sg.popup_yes_no("Delete all items?", title="Confirm", font=("Helvetica", 10))
                if answer == "No":
                    continue
                todos.clear()
                main_functions.write_todo_file(todos)
                window["todos"].update(values=todos)
                window["To-Do"].update(value=[])

        case "Exit":
            break

        case "todos":
            try:
                window["To-Do"].update(value=values["todos"][0])
            except IndexError:
                continue

        case sg.WIN_CLOSED:
            break

window.close()
