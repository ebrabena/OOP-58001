from tkinter import *
window = Tk()

window.geometry("300x300+10+20")
window.title("Father of Computer")

label = Label(window, text="Charles Babbage", fg="black", bg="cyan", font=("Arial", 20))
label.place(x=40, y=100)

window.mainloop()