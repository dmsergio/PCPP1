import tkinter as tk

window = tk.Tk()

button_1 = tk.Button(window, text="Regular button");
button_2 = tk.Button(window, text="Another button")

button_1.pack()
button_2.pack()

button_1["anchor"] = tk.E
button_1["width"] = 20  # pixels!

button_2["anchor"] = tk.W
button_2["width"] = 20
button_2["height"] = 3  # rows

window.mainloop()
