import tkinter
from tkinter import *
from tkinter import messagebox

def btnclick():
    messagebox.showinfo("Message","Button is clicked")

root=tkinter.TK()

photo=PhotoImage(file="group.png")

btn=Button(
    root,
    image=photo,
    command=btnclick,
)
btn.pack()
root.mainloop()