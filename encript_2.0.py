import tkinter as tk
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
import secrets, pyperclip

window = tk.Tk()

window.geometry("1000x500")
label = tk.Label(window, text="Encription")
label.pack()

entry_widget = tk.Entry(window, width=50, font=("Arial", 20))
entry_widget.place(x=500, y=50, anchor=tk.CENTER)

label1 = tk.Label(window, text="", width=75, font=("Ariel", 20))
label1.place(x=500, y=450, anchor=tk.CENTER)

#! secret key generation
key = secrets.token_bytes(16)
iv = secrets.token_bytes(16)

def encrypt():
    #*create an AES cipher object 
    cipher = AES.new(key, AES.MODE_CBC, iv)
    user_input = entry_widget.get()
    # makes into bytes
    text_bytes = user_input.encode('UTF-8')
    #* encript the message
    plain_text = text_bytes
    padded_plain_text = pad(plain_text, AES.block_size)
    cipher_text = cipher.encrypt(padded_plain_text)
    
    label1.configure(text=str(cipher_text))
    # converts to hex
    cipher_text_str = cipher_text.hex()
    # copy to clipboard
    pyperclip.copy(cipher_text_str)

encrypt_button = tk.Button(window, text="encrypt", width=10, height=2, command=encrypt)
encrypt_button.configure(font=("Ariel", 20))
encrypt_button.place(x=250, y=150, anchor=tk.CENTER)

def decrypt():
    cipher = AES.new(key, AES.MODE_CBC, iv)
    user_input = entry_widget.get()
    #* hex to byte
    cipher_text = bytes.fromhex(user_input)
    #* decripts the message
    decrypted_padded_plaintext = cipher.decrypt(cipher_text)
    plaint_text = unpad(decrypted_padded_plaintext, AES.block_size)
    
    label1.configure(text=str(plaint_text))
    
    
decrypt_button = tk.Button(window, text="decrypt", width=10, height=2, command=decrypt)
decrypt_button.configure(font=("Ariel", 20))
decrypt_button.place(x=750, y=150, anchor=tk.CENTER)
#TODO add different types of encription

window.mainloop()