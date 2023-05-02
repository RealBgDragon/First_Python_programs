import tkinter as tk

window = tk.Tk()

window.geometry("500x500")

label = tk.Label(window, text="Calculator")
label.pack()

entry_widget1 = tk.Entry(window, width=30, font=("Ariel", 20))
entry_widget1.place(x=250, y=50, anchor=tk.CENTER)

entry_widget2 = tk.Entry(window, width=30, font=("Ariel", 20))
entry_widget2.place(x=250,y=125, anchor=tk.CENTER)

label1 = tk.Label(window, font=("Ariel", 20))
label1.place(x=250, y=450, anchor=tk.CENTER)

x = 0
y = 0
def add():
    x = float(entry_widget1.get())
    y = float(entry_widget2.get())
    ans = x + y
    label1.configure(text=str(ans))
    
add_button = tk.Button(window, text="+", width=5, height=1, command=add)
add_button.configure(font=("Ariel", 20))
add_button.place(x=25, y=200)

def sub():
    x = float(entry_widget1.get())
    y = float(entry_widget2.get())
    ans = x - y
    label1.configure(text=str(ans))

sub_button = tk.Button(window, text="-", width=5, height=1, command=sub)
sub_button.configure(font=("Ariel", 20))
sub_button.place(x = 125, y = 200)


window.mainloop()