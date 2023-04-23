import tkinter as tk


window = tk.Tk()

button_1 = tk.Button(window, text="Button #1")
button_2 = tk.Button(window, text="Button #2")
button_3 = tk.Button(window, text="Button #3")

button_1.grid(column=0, row=0)
button_2.grid(column=1, row=1)
button_3.grid(column=0, row=2)

window.mainloop()
