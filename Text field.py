from tkinter import *
window = Tk()

window.geometry("300x300+10+20")
window.title("Text field")

txtfld = Entry(window, bd=1, width=30)
txtfld.place(x=50, y=100)

window.mainloop()