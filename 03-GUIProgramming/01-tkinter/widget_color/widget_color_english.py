import tkinter as tk


window = tk.Tk()

button = tk.Button(
    window,
    text="Button #1",
    fg="blue",
    activeforeground="dark blue",
)

button.pack()

window.mainloop()
