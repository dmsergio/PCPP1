import tkinter as tk
from tkinter import messagebox


def click(event=None):
    msg = "I love clicks!"
    if event is not None:
        msg = f"Clicked from button {event.num}!"
    messagebox.showinfo("Click!", msg)

def hover(event=None):
    print("Venga daleeeeeeeeeee!")


window = tk.Tk()
label = tk.Label(window, text="Label")
label.bind("<Button-1>", click)   # Line I
label.pack()

button = tk.Button(window, text="Button", command=click)
button.bind("<Enter>", hover)
button.pack(fill=tk.X)

frame = tk.Frame(window, height=30, width=100, bg="#55BF40")
frame.bind("<Button-1>", click)
frame.bind("<Button-2>", click)
frame.bind("<Button-3>", click)
frame.pack()

window.mainloop()
