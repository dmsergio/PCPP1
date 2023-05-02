import tkinter as tk
from tkinter import messagebox


def clicked():
    messagebox.showinfo(title="Click", message="I love clicks!")

window = tk.Tk()

label = tk.Label(window, text="Label")
label.pack()

button = tk.Button(window, text="Button", command=clicked)
button.pack(fill=tk.X)

frame = tk.Frame(window, height=30, width=100, background="#55BF40")
frame.pack()

window.mainloop()
