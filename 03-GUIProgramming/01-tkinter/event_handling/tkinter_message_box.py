import tkinter as tk
from tkinter import messagebox


def clicked():
    messagebox.showinfo(title="Info", message="This is a info\nmessage")

window = tk.Tk()

button_1 = tk.Button(window, text="Show info", command=clicked)
button_1.pack()

button_destroy = tk.Button(window, text="Close", command=window.destroy)
button_destroy.pack()

window.mainloop()
