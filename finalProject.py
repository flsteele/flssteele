import random
from tkinter import *
import tkinter.messagebox as showinfo

num = [1, 2, 3, 4, 5, 6, 7, 8, 9]

def on_closing():
    if showinfo.askokcancel("Quit", "Do you want to quit?"):
        window.destroy()

def check_ans(var1):
    resultAns = resultMultiply()
    if var1.get() == str(resultAns):
        correct = Label(window, text="Correct!", fg="green", font=("Courier", 16))
        correct.place(relx=0.16, rely=0.14, relwidth=0.73, relheight=0.23)
    else:
        wrong = Label(window, text=f"{practice.num1update}*{practice.num2update} is {resultAns}", fg="red", font=("Courier", 16))
        wrong.place(relx=0.16, rely=0.14, relwidth=0.73, relheight=0.23)

def practice():
    input.delete(0, 'end')
    input.focus_set()
    practice.num1update = random.choice(num)
    practice.num2update = random.choice(num)
    newQuestion = Label(window, text=f"What is {practice.num1update}*{practice.num2update} ?", font=("Courier", 16))
    newQuestion.place(relx=0.16, rely=0.14, relwidth=0.7, relheight=0.23)

def resultMultiply():
    practice
    return practice.num1update * practice.num2update

window = Tk() #create an instance of tkinter frame
window.title("Practice Multiplicatication")#Tittle of the window
window.geometry("350x300")#set the size
window.eval('tk::PlaceWindow . center') #center of screen
window.resizable(False, False)#disable resize

practice = Button(window, text="Practice", command=practice)
practice.place(relx=0.10, rely=0.64)

input = Entry(window, justify='center', font=('Courier', 20,'bold'))
input.place(relx=0.35, rely=0.4, relwidth=0.30, relheight=0.20)

check = Button(window, text="Check", command=lambda: check_ans(input))
check.place(relx=0.65, rely=0.64)

window.protocol("WM_DELETE_WINDOW", on_closing)
window.mainloop()
