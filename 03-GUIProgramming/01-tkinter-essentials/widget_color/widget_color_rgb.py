import tkinter as tk


window = tk.Tk()

button = tk.Button(
    window,
    text="Button #1",
    fg="#FFA07A",
    activeforeground="#FF69B4",
)

button.pack()

window.mainloop()
