import tkinter as tk


window = tk.Tk()

button = tk.Button(window, text="My button", command=lambda: None)
button.pack()

button["text"] = "Hey!"

window.mainloop()
