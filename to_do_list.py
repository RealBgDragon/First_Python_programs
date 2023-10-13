from tkinter import *
from tkinter import messagebox
from tkinter import filedialog
from tkcalendar import DateEntry
import json
from datetime import date

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
# array for date
dates = []

menu = Menu(window)
window.config(menu=menu)

# popup setup
def popup_setup(popup, submit):
    # label for the popup
    labelp = Label(popup, text="Enter you data:")
    labelp.pack()
    # entry for the popup
    entry = Entry(popup)
    entry.pack()
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
    return entry, entry_more_info, date_entry

# add_button methood
def add_task():
    # submit button
    def submit():
        task = entry.get()
        more_info_temp = entry_more_info.get()
        date_temp = date_entry.get_date()  # Get the selected date.
        date_str = date_temp.strftime("%Y-%m-%d")  # Convert date to string.
        if len(task) == 0 or len(more_info_temp) == 0:
            messagebox.showerror("Please enter the requered info!")
            return
        popup.destroy()
        task_list.insert(END, task)
        additional_info.append(more_info_temp)
        dates.append(date_str)
        
    # creates popup    
    popup = Toplevel()
    popup.title("Add task!")
    popup.geometry("250x250")
    entry, entry_more_info, date_entry = popup_setup(popup,submit)
    

def edit_task():
    def submit():
        task = entry.get()
        more_info_temp = entry_more_info.get()
        date_temp = date_entry.get_date()
        date_str = date_temp.strftime("%Y-%m-%d")
        if len(task) == 0 or len(more_info_temp) == 0:
            messagebox.showerror("Please enter the requered info!")
            return
        popup.destroy()
        task_list.delete(task_index)
        additional_info.pop(task_index)
        dates.pop(task_index)
        task_list.insert(task_index, task)
        additional_info[task_index] = more_info_temp
        dates[task_index] = date_str
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
    popup.geometry("250x250")
    entry, entry_more_info, date_entry = popup_setup(popup,submit)

# delete task
def delete_task():
    selection = task_list.curselection()
    
    if len(selection) == 0:
        messagebox.showerror("Error!", """No task selected.""")
        return
    task_index = selection[0]
    
    task_list.delete(task_index)
    additional_info.pop(task_index)
    dates.pop(task_index)

def delete_task_delete(event):
    delete_task()
# delete with delete
task_list.bind("<Delete>", delete_task_delete)

    

# more info function
def more_info(event):
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
    task_name_text = Label(popup, text=f"Task: {selected_task}")
    task_name_text.place(anchor=CENTER, x=150, y=10)
    # selected task info
    selected_task_info = additional_info[task_index]
    # additional info for the task
    task_info_label = Label(popup, text="Additional task info:")
    task_info_label.place(anchor=CENTER, x=150, y=60)
    task_info_text = Label(popup, text=selected_task_info)
    task_info_text.place(anchor=CENTER, x=150, y=80)
    # date task info
    selected_date_info = dates[task_index]
    # additional info for the date
    date_info_label = Label(popup, text="Date:")
    date_info_label.place(anchor=CENTER, x=150, y=100)
    date_info_text = Label(popup, text=selected_date_info)
    date_info_text.place(anchor=CENTER, x=150, y=120)
    # past due
    today = date.today()
    current_date = today.strftime("%Y-%m-%d")
    if dates[task_index] < current_date:
        past_due_label = Label(popup, font=("Ariel", 16), text="!task is past due!", fg="red")
        past_due_label.place(anchor=CENTER, x=150, y=150)
    
"""
def mark_task_complete():
    selection = task_list.curselection()
    if len(selection) == 0:
        messagebox.showerror("Error!", "No task selected!")
        return
    task_index = selection[0]
    selected_task = task_list.get(task_index)
    print("complete")
    """
# can double click to open additional infos   
task_list.bind("<Double-Button-1>", more_info)
    
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
#more_info_button = Button(window, text="More info", command=more_info)
#more_info_button.pack(side=LEFT, anchor=SW)
# mark task complete button
#task_complete_button = Button(window, text="Mark task complete", command=mark_task_complete)
#task_complete_button.pack(side=LEFT, anchir=SW)

file_menu = Menu(menu, font=("Arial", 10))

#* exit the program
def exit_program():
    window.destroy()
    
# new task
def new_task_list():
    task_list.delete(0, END)
    additional_info.clear()
    dates.clear()
# save task
def open_task_list():
    filename = filedialog.askopenfilename(filetypes=[("JSON files", "*.json")])
    if not filename:
        return  # User canceled open dialog

    with open(filename, 'r') as f:
        data = json.load(f)
    for task in data['tasks']:
        task_list.insert(END, task)
    additional_info[:] = data['additional_info']
    dates[:] = data['dates']
# load task
def save_task_list():
    filename = filedialog.asksaveasfilename(defaultextension=".json", filetypes=[("JSON files", "*.json")])
    if not filename:
        return  # User canceled save dialog

    data = {
        'tasks': list(task_list.get(0, END)), 
        'additional_info': additional_info, 
        'dates': dates
    }
    with open(filename, 'w') as f:
        json.dump(data, f)
# files list
file_menu.add_command(label="New Task List", command=new_task_list)
file_menu.add_command(label="Open Task List", command=open_task_list)
file_menu.add_command(label="Save Task List", command=save_task_list)

file_menu.add_separator()
file_menu.add_command(label="Exit", command=exit_program)
menu.add_cascade(label="File", menu=file_menu)

#! has to exist
window.mainloop()
