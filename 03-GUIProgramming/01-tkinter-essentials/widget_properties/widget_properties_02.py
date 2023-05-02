import tkinter as tk

window = tk.Tk()

button_1 = tk.Button(window, text="Ordinary button");
button_2 = tk.Button(window, text="Colorful button")

button_1.pack()
button_2.pack()

button_2.config(bg ="#000000")
button_2.config(fg ="yellow")
button_2.config(activeforeground ="#FF0000")
button_2.config(activebackground ="green")

window.mainloop()
