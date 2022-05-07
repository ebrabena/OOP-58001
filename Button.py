from tkinter import *
window = Tk()

window.geometry("400x300+10+20")
window.title("Button")

button = Button(window, text="Color", fg="red", bg="blue", activeforeground="red", activebackground="yellow", font=("Verdana", 12))
button.place(x=50, y=70)
button1 = Button(window, text="<---Click to change the color of the button")
button1.place(x=120, y=70)

window.mainloop()