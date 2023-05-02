import tkinter as tk


window = tk.Tk()

label = tk.Label(window, text="Little label")
label.pack()

frame = tk.Frame(window, height=10, width=100, bg="gray")
frame.pack()

button = tk.Button(window, text="Button")
button.pack(fill=tk.X)

switch = tk.IntVar()
switch.set(1)

check_button = tk.Checkbutton(window, text="Check button", variable=switch)
check_button.pack()

entry = tk.Entry(window, width=50)
entry.pack()

radiobutton_1 = tk.Radiobutton(window, text="Off", variable=switch, value=0)
radiobutton_2 = tk.Radiobutton(window, text="On", variable=switch, value=1)
radiobutton_1.pack()
radiobutton_2.pack()

window.mainloop()
