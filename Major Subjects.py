from tkinter import *
window = Tk()

window.geometry("300x300+10+20")
window.title("Major Subjects")

data = "reading", "writing", "arithmetic", "coding"
lb = Listbox(window, height=5, selectmode="multiple")
for num in data:
    lb.insert(END, num)
    lb.place(x=70, y=100)

window.mainloop()