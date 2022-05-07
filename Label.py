from tkinter import *
window = Tk()

window.geometry("300x300+10+20")
window.title("Label")

label = Label(window, text="Laboratory Activity 5")
label1 = Label(window, text="Submitted to: Mam Sayo")
label.place(x=100, y=100)
label1.place(x=90, y=130)

window.mainloop()