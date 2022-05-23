from tkinter import *

window = Tk()
window.title("Smallest Number Determiner")
window.geometry("500x80")

def det():
    L = []
    L.append(eval(num1.get()))
    L.append(eval(num2.get()))
    L.append(eval(num3.get()))
    numS.set(min(L))

lbl1 = Label(window, text = "Enter the first number:")
lbl1.grid(row = 1, column = 0, sticky = W)
num1 = StringVar()
val1 = Entry(window, bd = 3 ,textvariable = num1)
val1.grid(row = 1, column = 1)

lbl2 = Label(window,text = "Enter the second number:")
lbl2.grid(row = 2, column = 0)
num2=StringVar()
val2 = Entry(window,bd = 3,textvariable = num2)
val2.grid(row = 2,column = 1)

lbl3 = Label(window,text = "Enter the third number:")
lbl3.grid(row = 3, column = 0, sticky = W)
num3 = StringVar()
val3 = Entry(window, bd = 3, textvariable = num3)
val3.grid(row = 3, column = 1)

btn1 = Button(window, text = "Find the smallest number", command = det)
btn1.grid(row = 2, column = 2)
val4 = Label(window, text = "The smallest number is:")
val4.grid(row = 3, column = 2, sticky = W)
numS = StringVar()

lbl4 = Label(window, bd = 3,textvariable = numS)
lbl4.grid(row = 3, column = 3)

mainloop()