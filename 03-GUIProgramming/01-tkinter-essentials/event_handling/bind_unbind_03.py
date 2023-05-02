import tkinter as tk
from tkinter import messagebox


def hello(dummy):
    messagebox.showinfo("", "Hello!")


window = tk.Tk()

button = tk.Button(window, text="On/Off")
label = tk.Label(window, text="Label")
frame = tk.Frame(window, bg="yellow", width=100, height=20)

button.pack()
label.pack()
frame.pack()

# bind the event to all widgets inside window
window.bind_all("<Button-1>", hello)
# window.unbind_all("<Button-1>")

window.mainloop()
