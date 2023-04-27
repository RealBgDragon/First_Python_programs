import tkinter as tk
from cryptography.fernet import Fernet, MultiFernet
from cryptography.hazmat.primitives.asymmetric import rsa, padding
from cryptography.hazmat.primitives import serialization, hashes
import pyperclip

window = tk.Tk()

window.geometry("1000x500")
label = tk.Label(window, text="Encryption")
label.pack()

entry_widget = tk.Entry(window, width=50, font=("Arial", 20))
entry_widget.place(x=500, y=50, anchor=tk.CENTER)

label1 = tk.Label(window, text="", width=75, font=("Ariel", 20))
label1.place(x=500, y=450, anchor=tk.CENTER)

# generate key pair
private_key = rsa.generate_private_key(
    public_exponent=65537,
    key_size=2048
)
public_key = private_key.public_key()

# serialize public key to bytes
public_key_bytes = public_key.public_bytes(
    encoding=serialization.Encoding.PEM,
    format=serialization.PublicFormat.SubjectPublicKeyInfo
)

# encrypt message with public key
def encrypt():
    user_input = entry_widget.get().encode('utf-8')
    cipher = public_key.encrypt(
        user_input,
        padding.OAEP(
            mgf=padding.MGF1(algorithm=hashes.SHA256()),
            algorithm=hashes.SHA256(),
            label=None
        )
    )
    label1.configure(text=str(cipher))
    # copy to clipboard
    cipher_text_str = cipher.hex()
    pyperclip.copy(cipher_text_str)

encrypt_button = tk.Button(window, text="Encrypt", width=10, height=2, command=encrypt)
encrypt_button.configure(font=("Ariel", 20))
encrypt_button.place(x=250, y=150, anchor=tk.CENTER)

# decrypt message with private key
def decrypt():
    user_input = entry_widget.get().encode('utf-8')
    cipher_text = bytes.fromhex(user_input.decode('utf-8'))
    plain_text = private_key.decrypt(
        cipher_text,
        padding.OAEP(
            mgf=padding.MGF1(algorithm=hashes.SHA256()),
            algorithm=hashes.SHA256(),
            label=None
        )
    )
    label1.configure(text=str(plain_text.decode('utf-8')))

decrypt_button = tk.Button(window, text="Decrypt", width=10, height=2, command=decrypt)
decrypt_button.configure(font=("Ariel", 20))
decrypt_button.place(x=750, y=150, anchor=tk.CENTER)

window.mainloop()