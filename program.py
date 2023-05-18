from tkinter import *
from tkinter import messagebox
from tkinter.filedialog import asksaveasfilename
from tkinter.filedialog import askopenfilename
from tkcalendar import DateEntry
import os

window = Tk()

label = Label(window, width=20, font=("Ariel", 16), text="To-Do list")
label.pack()

window.geometry("750x750")

task_list = Listbox(window)
task_list.pack(side=RIGHT, fill=BOTH, expand=TRUE)

scrollbar = Scrollbar(window)
scrollbar.pack(side=RIGHT, fill=Y)
task_list.config(yscrollcommand=scrollbar.set)
scrollbar.config(command=task_list.yview)


# array of additional info
additional_info = []

menu = Menu(window)
window.config(menu=menu)

#add_button methood
def add_task():
    # submit button
    def submit():
        task = entry.get()
        more_info_temp = entry_more_info.get()
        additional_info.append(more_info_temp)
        if len(task) == 0 or len(more_info_temp) == 0:
            messagebox.showerror("Please enter the requered info!")
            return
        popup.destroy()
        task_list.insert(END, task)
    # creates popup    
    popup = Toplevel()
    popup.title("Add task!")
    popup.geometry("250x250")
    # label for the popup
    labelp = Label(popup, text="Enter your info:")
    labelp.place(anchor=CENTER, x=125, y=10)
    # entry for the popup
    entry = Entry(popup)
    entry.place(anchor=CENTER, x=125, y=50)
    # aditional info label
    additional_info_label = Label(popup, text="Enter details:")
    additional_info_label.place(anchor=CENTER, x=125, y=75)
    # more info entry
    entry_more_info = Entry(popup, width=35)
    entry_more_info.place(anchor=CENTER, x=125, y=100)
    # date label
    date_label = Label(popup, text="Enter due date:")
    date_label.place(anchor=CENTER, x=125, y=125)
    #date entry
    date_entry = DateEntry(popup)
    date_entry.place(anchor=CENTER, x=125, y=150)
    # submit button
    submit_button = Button(popup, text="Submit!", command=submit)
    submit_button.place(anchor=CENTER, x=125, y=200)
    
    
# edit task
def edit_task():
    def submit():
        data = entry.get()
        if len(data) == 0:
            messagebox.showerror("Please enter task name!")
            return
        popup.destroy()
        task_list.delete(task_index)
        task_list.insert(task_index, data)
    # mark selected task
    selection = task_list.curselection()
    # chek for the selection
    if len(selection) == 0:
        messagebox.showerror("Please select task!")
        return
    # index of the selected task
    task_index = selection[0]
    # creates popup
    popup = Toplevel()
    popup.title("Edit task!")
    popup.geometry("250x100")
    # label for the popup
    labelp = Label(popup, text="Enter you data:")
    labelp.pack()
    # entry for the popup
    entry = Entry(popup)
    entry.pack()
    # submit button 
    submit_button = Button(popup, text="Submit!", command=submit)
    submit_button.pack()

# delete task
def delete_task():
    selection = task_list.curselection()
    
    if len(selection) == 0:
        messagebox.showerror("Error!", "No task selected.")
        return
    task_index = selection[0]
    
    task_list.delete(task_index)

#TODO finish the more info function
def more_info():
    selection = task_list.curselection()
    if len(selection) == 0:
        messagebox.showerror("Error!", "No task selected.")
        return
    task_index = selection[0]
    selected_task = task_list.get(task_index)
    popup = Toplevel()
    popup.title(f"Additional info for {selected_task}")
    popup.geometry("300x300")
    # name of the task
    task_name_label = Label(popup, text=f"Task: {selected_task}")
    task_name_label.place(anchor=CENTER, x=150, y=10)
    # selected task info
    selected_task_info = additional_info[task_index]
    # additional info for the task
    task_info_label_label = Label(popup, text=f"Additional task info:")
    task_info_label_label.place(anchor=CENTER, x=150, y=60)
    task_info_label = Label(popup, text=selected_task_info)
    task_info_label.place(anchor=CENTER, x=150, y=80)
    
# add button
add_button = Button(window, text="Add task", command=add_task)
add_button.pack(side=LEFT, anchor=NW)
# edit button
edit_button = Button(window, text="Edit Task", command=edit_task)
edit_button.pack(side=LEFT, anchor=NW)
# delete button
delete_button = Button(window, text="Delete", command=delete_task)
delete_button.pack(side=LEFT, anchor=NW)
# more info button
more_info_button = Button(window, text="More info", command=more_info)
more_info_button.pack(side=LEFT, anchor=SW)

file_menu = Menu(menu, font=("Arial", 10))

#* exit the program
def exit_program():
    window.destroy()
    
# new task
def new_task_list():
    for i in range(task_list.size()):
        task_list.delete(i)

# open task
def open_task_list():
    filename = askopenfilename(initialdir=os.path.expanduser("~/Desktop/To-Do list files"), defaultextension=".txt")
    if filename:
        with open(filename, "r") as f:
            contents = f.read()
            task_list.delete(0, END)
            for i in contents.split("\n"):
                if i.strip():
                    task_list.insert(END, i)

# save task list
def save_task_list():
    filename = asksaveasfilename(initialdir=os.path.expanduser("~/Desktop/To-Do list files"), defaultextension=".txt")
    if filename:
        with open(filename, "w") as f:
            for i in range(task_list.size()):
                f.write(task_list.get(i) + "\n")
    
file_menu.add_command(label="New Task List", command=new_task_list)
file_menu.add_command(label="Open Task List", command=open_task_list)
file_menu.add_command(label="Save Task List", command=save_task_list)

file_menu.add_separator()
file_menu.add_command(label="Exit", command=exit_program)
menu.add_cascade(label="File", menu=file_menu)

#TODO add past due and shit


window.mainloop()