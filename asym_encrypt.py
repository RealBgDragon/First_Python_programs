import tkinter as tk
from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP
import base64, pyperclip

window = tk.Tk()

window.geometry("1000x500")
label = tk.Label(window, text="Encription")
label.pack()

entry_widget = tk.Entry(window, width=30, font=("Arial", 20))
entry_widget.place(x=500, y=50, anchor=tk.CENTER)

label1 = tk.Label(window, text="", width=75, font=("Ariel", 20))
label1.place(x=500, y=450, anchor=tk.CENTER)

#! secret key generation
key = RSA.generate(2048)

def encrypt(): 
    user_input = entry_widget.get()
    #*create an RSA cipher object
    cipher = PKCS1_OAEP.new(key.public_key())
    # makes into bytes
    text_bytes = user_input.encode('UTF-8')
    #* encript the message
    cipher_text_bytes = cipher.encrypt(text_bytes)
    #* as base64 for safe trans
    cipher_text_base64 = base64.b64encode(cipher_text_bytes).decode('utf-8')
    
    label1.configure(text=cipher_text_base64)
    # copy to clipboard
    pyperclip.copy(cipher_text_base64)

encrypt_button = tk.Button(window, text="encrypt", width=10, height=2, command=encrypt)
encrypt_button.configure(font=("Ariel", 20))
encrypt_button.place(x=250, y=150, anchor=tk.CENTER)

def decrypt():
    user_input = entry_widget.get()
    cipher_text_base64 = user_input
    #* Decode from base64
    cipher_text_bytes = base64.b64decode(cipher_text_base64.encode('utf-8'))
    #* RSA object
    cipher = PKCS1_OAEP.new(key)
    #* decripts the message
    message_bytes = cipher.decrypt(cipher_text_bytes)
    plaint_text = message_bytes.decode('utf-8')
    
    label1.configure(text=str(plaint_text))
    
    
decrypt_button = tk.Button(window, text="decrypt", width=10, height=2, command=decrypt)
decrypt_button.configure(font=("Ariel", 20))
decrypt_button.place(x=750, y=150, anchor=tk.CENTER)
#TODO add different types of encription

window.mainloop()