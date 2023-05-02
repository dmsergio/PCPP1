import tkinter as tk


window = tk.Tk()

button = tk.Button(window, text="My button", command=lambda: None)
button.pack()

print(button.cget("text"))
button.config(text="Hey!")

window.mainloop()
