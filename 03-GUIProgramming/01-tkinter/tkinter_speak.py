import tkinter
from tkinter import messagebox


def Click():
    response = messagebox.askquestion("Quit application", "Are you sure?")
    if response == "yes":
        skylight.destroy()


skylight = tkinter.Tk()
skylight.title("Skylight")

button = tkinter.Button(skylight, text="Bye!", command=Click)
button.place(x=10, y=10)

skylight.mainloop()
