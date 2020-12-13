# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.
import tkinter as tk
from tkinter import filedialog
from tkinter import *
from tkinter import simpledialog
import blowfish

class Cryptext:

    def __init__(self, master):
        master.title("Untitled -- Cryptext")
        master.geometry("1200x700")

        self.master = master

        self.textarea = tk.Text(master)
        self.scroll = tk.Scrollbar(master, command=self.textarea.yview)
        self.textarea.configure(yscrollcommand=self.scroll.set)
        self.textarea.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        self.scroll.pack(side=tk.RIGHT, fill=tk.Y)

        self.menu = Menu(self)

    def new_file(self):
        self.textarea.delete(1.0, tk.END)
        self.filename = None



    def save_encrypt(self):
        #TODO: save & encrypt
        def save(self):
            file_path = filedialog.asksaveasfilename(initialdir = "/",
            title = "Save file",
            filetypes = (("Text files","*.txt"),("all files","*.*")))
            self.filename = file_path

            if (file_path == self.filename):
                file_path = self.filename
                encrypt(self, file_path)

            else:
                encrypt(file_path)

        def encrypt(self, file_path):
            with open(file_path, 'w') as the_file:
                key = simpledialog.askstring("Set Key",
                "Please create a key between 4-56 chars to protect your file. This key cannot be retrieved.")
                res = ''.join(format(ord(i), 'b') for i in key)
                print(res)
                cipher = blowfish.Cipher(res)
                data = the_file.get()
                data_encrypted = b"".join(cipher.encrypt_ecb(data))
                data_decrypted = b"".join(cipher.decrypt_ecb(data_encrypted))
                the_file.write(data_encrypted)
                file.close()

        save(self)





    def open_file():
        #TODO: should be able to open and edit file with key authentication
        pass

class Menu:

    def __init__(self, parent):
        menu = tk.Menu(parent.master)
        parent.master.config(menu=menu)

        file_dropdown = tk.Menu(menu, tearoff=0)
        file_dropdown.add_command(label = "New File", command=parent.new_file)
        file_dropdown.add_command(label = "Save and Encrypt", command = parent.save_encrypt)
        file_dropdown.add_command(label = "Open File")


        menu.add_cascade(label="Menu", menu= file_dropdown)


if __name__ == '__main__':
    master = tk.Tk()
    ct = Cryptext(master)
    master.mainloop()
