import tkinter as tk
from tkinter import messagebox


def click(event=None):
    if event is None:
        messagebox.showinfo("Click!", "I love clicks!")
    else:
        msg = f"x={event.x}, y={event.y}, num={event.num}, type={event.type}"
        messagebox.showinfo("Click!", msg)


window = tk.Tk()
label = tk.Label(window, text="Label")
label.bind("<Button-1>", click)
label.pack()

button = tk.Button(window, text="Button", command=click)
button.pack(fill=tk.X)

frame = tk.Frame(window, height=30, width=100, bg="#55BF40")
frame.bind("<Button-1>", click)
frame.pack()

window.mainloop()
