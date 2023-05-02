import tkinter as tk

window = tk.Tk()

window.geometry("500x600")

label = tk.Label(window, width=30, font=("Ariel", 20), text="Wartunder calculator")
label.pack()

entry_wiget_1 = tk.Entry(window, width=30, font=("Ariel", 20))
entry_wiget_1.place(x=250, y=50, anchor=tk.CENTER)
   
label_ans = []

for i in range(9):
    ans_label = tk.Label(window, width=20, font=("Ariel", 20))
    ans_label.place(x=250, y=150 + 50*i, anchor=tk.CENTER)
    label_ans.append(ans_label)

x = 1

def calcualte():
    x = int(entry_wiget_1.get())
    
    for i in range(1, 10):
        result = x * i
        label_ans[i-1].config(text="За {}: {}".format(i, result))

calcualte_button = tk.Button(window, text="Find range", font=("Ariel", 20), command=calcualte)
calcualte_button.place(x=250, y=100, anchor=tk.CENTER)
    
window.mainloop()