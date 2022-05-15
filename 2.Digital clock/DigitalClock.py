from tkinter import *
import time

root = Tk()
root.title('Digital Clock')
root.geometry('800x400')


def myTime():
    myText = time.strftime("%I:%M:%S %p")
    myText2 = time.strftime("%A")
    myLabel.config(text=myText)
    myLabel2.config(text=myText2)
    myLabel.after(1000, myTime)


myLabel = Label(root, text='', font=(
    'Arial', 72), fg='white', bg='black')
myLabel.pack()
myLabel2 = Label(root, text="", font=('Arial', 24))
myLabel2.pack()

myTime()

root.mainloop()
