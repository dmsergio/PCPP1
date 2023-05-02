import tkinter as tk


def flip_focus():
    if window.focus_get() is button_1:
        button_2.focus_set()
    elif window.focus_get() is button_2:
        button_3.focus_set()
    else:
        button_1.focus_set()
    window.after(1000, flip_focus)


window = tk.Tk()
button_1 = tk.Button(window, text="First")
button_1.pack()
button_2 = tk.Button(window, text="Second")
button_2.pack()
button_3 = tk.Button(window, text="Third")
button_3.pack()
window.after(1000, flip_focus)
window.mainloop()
