from tkinter import *

window = Tk()

label = Label(window, width=20, font=("Ariel", 16), text="To-Do list")
label.pack()

window.geometry("500x750")

task_list = Listbox(window)
task_list.pack(side=RIGHT, fill=BOTH, expand=TRUE)

#task entry
task_entry = Entry(window)
task_entry.pack(side=LEFT)


scrollbar = Scrollbar(window)
scrollbar.pack(side=RIGHT, fill=Y)
task_list.config(yscrollcommand=scrollbar.set)
scrollbar.config(command=task_list.yview)

menu = Menu(window)
window.config(menu=menu)

#add_button methood

def add_task():
    task = task_entry.get()
    #insert into the end
    task_list.insert(END, task)
    #clear the widget
    task_entry.delete(0, END)

# task entry button
add_button = Button(window, text="Add task", command=add_task)
add_button.pack(side=LEFT)





file_menu = Menu(menu, font=("Arial", 10))




#* exit the program
def exit_program():
    window.destroy()
    

def new_task_list():
    print("New Task List")

def open_task_list():
    print("Open Task List")

def save_task_list():
    print("Save Task List")
    
    
#! add a functionallity to the options
file_menu.add_command(label="New Task List", command=new_task_list)
file_menu.add_command(label="Open Task List", command=new_task_list)
file_menu.add_command(label="Save Task List", command=new_task_list)

file_menu.add_separator()
file_menu.add_command(label="Exit", command=exit_program)
menu.add_cascade(label="File", menu=file_menu)




window.mainloop()