import tkinter as tk
import hashlib

window = tk.Tk()

window.geometry("1000x500")
label = tk.Label(window, text="Encription")
label.pack()

entry_widget = tk.Entry(window, width=30, font=("Arial", 20))
entry_widget.place(x=25, y=50)

label1 = tk.Label(window, text="", width=75, font=("Ariel", 20))
label1.place(x=500, y=450, anchor=tk.CENTER)

def encrypt():
    user_input = entry_widget.get()
    password = str(user_input)
    #turn to binary
    password_bytes = password.encode('UTF-8')
    #creating SHA256 has object
    hash_obj = hashlib.sha256()
    #update with the password bytes
    hash_obj.update(password_bytes)
    #!get the hashed password in hex format
    hashed_password = hash_obj.hexdigest()
    print(hashed_password)
    label1.configure(text=str(hashed_password))

encrypt_button = tk.Button(window, text="encrypt", width=10, height=2, command=encrypt)
encrypt_button.configure(font=("Ariel", 20))
encrypt_button.place(x=250, y=150,anchor=tk.CENTER)

#TODO add different types of encription

window.mainloop()