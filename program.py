from tkinter import *
from tkinter import messagebox

window = Tk()

label = Label(window, width=20, font=("Ariel", 16), text="To-Do list")
label.pack()

window.geometry("750x750")

task_list = Listbox(window)
task_list.pack(side=RIGHT, fill=BOTH, expand=TRUE)

task_entry = Entry(window)
task_entry.pack(side=LEFT, anchor=NW)

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
    
def edit_task():
    selection = task_list.curselection()
    if len(selection) == 0:
        messagebox.showerror("Error", "No task selected")
        return
    task_index = selection[0]
    task_text = task_list.get(task_index)
    
    new_task_text = task_entry.get()
    if len(new_task_text) == 0:
        messagebox.showerror("Error", "Please enter a new task text")
        return
    task_list.delete(task_index)
    task_list.insert(task_index, new_task_text)
    
    task_entry.delete(0, END)
    

def delete_task():
    selection = task_list.curselection()
    
    if len(selection) == 0:
        messagebox.showerror("Error", "No task selected")
        return
    task_index = selection[0]
    task_text = task_list.get(task_index)
    
    task_list.delete(task_index)
    
# task entry button
add_button = Button(window, text="Add task", command=add_task)
add_button.pack(side=LEFT, anchor=NW)

edit_button = Button(window, text="Edit Task", command=edit_task)
edit_button.pack(side=LEFT, anchor=NW)

delete_button = Button(window, text="Delete", command=delete_task)
delete_button.pack(side=LEFT, anchor=NW)


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
file_menu.add_command(label="Open Task List", command=open_task_list)
file_menu.add_command(label="Save Task List", command=save_task_list)

file_menu.add_separator()
file_menu.add_command(label="Exit", command=exit_program)
menu.add_cascade(label="File", menu=file_menu)




window.mainloop()