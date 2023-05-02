import tkinter as tk

window = tk.Tk()

label_1 = tk.Label(window, height=3, width=50, text="arrow", cursor="arrow")
label_2 = tk.Label(window, height=3, width=50, text="clock", cursor="clock")
label_3 = tk.Label(window, height=3, width=50, text="heart", cursor="heart")
label_4 = tk.Label(window, height=3, width=50, text="spinning", cursor="spinning")
label_5 = tk.Label(window, height=3, width=50, text="xterm", cursor="xterm")

label_1.pack()
label_2.pack()
label_3.pack()
label_4.pack()
label_5.pack()

window.mainloop()
