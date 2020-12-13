
import random
from tkinter import *
from tkinter import messagebox,simpledialog
from PIL import Image, ImageTk
import os
import sys


window = Tk()
dashes=[]
chances=7
checkAnswer = []
img = Image.open('img1.jpg')
img = img.resize((200, 200), Image.ANTIALIAS)
img= ImageTk.PhotoImage(img)
panel = Label(window, image = img)
panel.grid(column=0, row=0)
answer = random.choice(open('file.txt').read().split('\n'))
    
def start():
    window.geometry('905x800')
    window.title('HANG MAN')
    window.config(bg = '#E7FFFF')
    
    for i in range(len(answer)):
        dashes.append('-')
    
    messagebox.showinfo("message","Welcome to HANGMAN GAME!!\n Guess the name of animals\n You have 7 chances to guess \n GOOD LUCK!")
    Label(window, text = dashes, font = ("Arial",20),fg="blue").grid(row = 0, column = 2)

    Button(window,text="exit-game",width=7,height=2,bg='red',command=lambda: exit()).grid(column=12,row=0)
    Label(window,text="Chances left: "+str(chances)).grid(row=5,column=0)

def exit():
    MsgBox = messagebox.askquestion ('Exit Application','Are you sure you want to exit game',icon = 'warning')
    if MsgBox == 'yes':
        window.destroy()
    
    else:
        restart_program()

def ExitApplication():
    MsgBox = messagebox.askquestion ('Exit Application','do you want to play again',icon = 'warning')
    if MsgBox == 'yes':
        restart_program()
    else:
        messagebox.showinfo('message', 'Good Bye!!')
        window.destroy()
        

def restart_program():
    python = sys.executable
    os.execl(python, python, * sys.argv)

def clicked(alphabet):
    global chances
    
    if alphabet in dashes:
        messagebox.showinfo("message","already used")
    
    for i in range(len(answer)):        
        if answer[i]==alphabet:
            dashes[i] = alphabet
            checkAnswer.append(alphabet)
            letter = Label(window, text = dashes, font = ("Arial",20),fg="red")
            letter.grid(row = 0, column = 2)
      
    checkAnswer.sort()
    ans=list(answer)
    ans.sort()
    #check to see if guessed is right
    if ans==checkAnswer:
        messagebox.showinfo("message","congrats!! you guessed right")
        ExitApplication()
    
    
    if alphabet not in answer:
        if chances==7:
            image = Image.open('img2.png')
            image = image.resize((200, 200), Image.ANTIALIAS)
            imgnew = ImageTk.PhotoImage(image)
            panel.configure(image=imgnew)
            panel.image = imgnew
            chances -=1
            Label(window,text="Chances left: "+str(chances)).grid(row=5,column=0)
            #print(chances)

        elif chances==6:
            image = Image.open('img3.png')
            image = image.resize((200, 200), Image.ANTIALIAS)
            imgnew = ImageTk.PhotoImage(image)
            panel.configure(image=imgnew)
            panel.image = imgnew
            chances -=1
            Label(window,text="Chances left: "+str(chances)).grid(row=5,column=0)
            #print(chances)
        elif chances==5:
            image = Image.open('img4.png')
            image = image.resize((200, 200), Image.ANTIALIAS)
            imgnew = ImageTk.PhotoImage(image)
            panel.configure(image=imgnew)
            panel.image = imgnew
            chances -=1
            Label(window,text="Chances left: "+str(chances)).grid(row=5,column=0)
            #print(chances)
        elif chances==4:
            image = Image.open('h5.png')
            image = image.resize((200, 200), Image.ANTIALIAS)
            imgnew = ImageTk.PhotoImage(image)
            panel.configure(image=imgnew)
            panel.image = imgnew
            chances -=1
            Label(window,text="Chances left: "+str(chances)).grid(row=5,column=0)
            #print(chances)
        elif chances==3:
            image = Image.open('h6.png')
            image = image.resize((200, 200), Image.ANTIALIAS)
            imgnew = ImageTk.PhotoImage(image)
            panel.configure(image=imgnew)
            panel.image = imgnew
            chances -=1
            Label(window,text="Chances left: "+str(chances)).grid(row=5,column=0)
            #print(chances)
        elif chances==2:
            image = Image.open('h7.png')
            image = image.resize((200, 200), Image.ANTIALIAS)
            imgnew = ImageTk.PhotoImage(image)
            panel.configure(image=imgnew)
            panel.image = imgnew
            chances -=1
            Label(window,text="Chances left: "+str(chances)).grid(row=5,column=0)
            #print(chances)
        elif chances==1:
            image = Image.open('hang.jpg')
            image = image.resize((200, 200), Image.ANTIALIAS)
            imgnew = ImageTk.PhotoImage(image)
            panel.configure(image=imgnew)
            panel.image = imgnew
            chances -=1
            Label(window,text="Chances left: "+str(chances)).grid(row=5,column=0)
            #print(chances)
            messagebox.showinfo("Loose","Sorry!!\nyou're Hanged!!!!! \n The answer is: "+answer)
            ExitApplication()
        
#function to display alphbabets in keyboard style   
def keyboard():

    btn1 = Button(window, text="a",bg="skyBlue", fg="Black",width=3,height=1,font=('Helvetica','20'),command=lambda: clicked("a"))
    btn1.grid(column=1, row=1)
    btn2 = Button(window, text="b",bg="skyBlue", fg="Black",width=3,height=1,font=('Helvetica','20'),command=lambda: clicked("b"))
    btn2.grid(column=2, row=1)
    btn3 = Button(window, text="c",bg="skyBlue", fg="Black",width=3,height=1,font=('Helvetica','20'),command=lambda: clicked("c"))
    btn3.grid(column=3, row=1)
    btn4 = Button(window, text="d",bg="skyBlue", fg="Black",width=3,height=1,font=('Helvetica','20'),command=lambda: clicked("d"))
    btn4.grid(column=4, row=1)
    btn5 = Button(window, text="e",bg="skyBlue", fg="Black",width=3,height=1,font=('Helvetica','20'),command=lambda: clicked("e"))
    btn5.grid(column=5, row=1)
    btn6 = Button(window, text="f",bg="skyBlue", fg="Black",width=3,height=1,font=('Helvetica','20'),command=lambda: clicked("f"))
    btn6.grid(column=6, row=1)
    btn7 = Button(window, text="g",bg="skyBlue", fg="Black",width=3,height=1,font=('Helvetica','20'),command=lambda: clicked("g"))
    btn7.grid(column=7, row=1)
    btn8 = Button(window, text="h",bg="skyBlue", fg="Black",width=3,height=1,font=('Helvetica','20'),command=lambda: clicked("h"))
    btn8.grid(column=8, row=1)

    btn9 = Button(window, text="i",bg="skyBlue", fg="Black",width=3,height=1,font=('Helvetica','20'),command=lambda: clicked("i"))
    btn9.grid(column=2, row=2)
    btn10 = Button(window, text="j",bg="skyBlue", fg="Black",width=3,height=1,font=('Helvetica','20'),command=lambda: clicked("j"))
    btn10.grid(column=3, row=2)
    btn11= Button(window, text="k",bg="skyBlue", fg="Black",width=3,height=1,font=('Helvetica','20'),command=lambda: clicked("k"))
    btn11.grid(column=4, row=2)
    btn12 = Button(window, text="l",bg="skyBlue", fg="Black",width=3,height=1,font=('Helvetica','20'),command=lambda: clicked("l"))
    btn12.grid(column=5, row=2)
    btn13 = Button(window, text="m",bg="skyBlue", fg="Black",width=3,height=1,font=('Helvetica','20'),command=lambda: clicked("m"))
    btn13.grid(column=6, row=2)
    btn14 = Button(window, text="n",bg="skyBlue", fg="Black",width=3,height=1,font=('Helvetica','20'),command=lambda: clicked("n"))
    btn14.grid(column=7, row=2)

    btn15= Button(window, text="o",bg="skyBlue", fg="Black",width=3,height=1,font=('Helvetica','20'),command=lambda: clicked("o"))
    btn15.grid(column=2, row=3)
    btn16 = Button(window, text="p",bg="skyBlue", fg="Black",width=3,height=1,font=('Helvetica','20'),command=lambda: clicked("p"))
    btn16.grid(column=3, row=3)
    btn17 = Button(window, text="q",bg="skyBlue", fg="Black",width=3,height=1,font=('Helvetica','20'),command=lambda: clicked("q"))
    btn17.grid(column=4, row=3)
    btn18 = Button(window, text="r",bg="skyBlue", fg="Black",width=3,height=1,font=('Helvetica','20'),command=lambda: clicked("r"))
    btn18.grid(column=5, row=3)
    btn19 = Button(window, text="s",bg="skyBlue", fg="Black",width=3,height=1,font=('Helvetica','20'),command=lambda: clicked("s"))
    btn19.grid(column=6, row=3)
    btn20 = Button(window, text="t",bg="skyBlue", fg="Black",width=3,height=1,font=('Helvetica','20'),command=lambda: clicked("t"))
    btn20.grid(column=7, row=3)

    btn21 = Button(window, text="u",bg="skyBlue", fg="Black",width=3,height=1,font=('Helvetica','20'),command=lambda: clicked("u"))
    btn21.grid(column=3, row=4)
    btn22 = Button(window, text="v", bg="skyBlue", fg="Black",width=3,height=1,font=('Helvetica','20'),command=lambda: clicked("v"))
    btn22.grid(column=4, row=4)
    btn23 = Button(window, text="w",bg="skyBlue", fg="Black",width=3,height=1,font=('Helvetica','20'),command=lambda: clicked("w"))
    btn23.grid(column=5, row=4)
    btn24 = Button(window, text="x",bg="skyBlue", fg="Black",width=3,height=1,font=('Helvetica','20'),command=lambda: clicked("x"))
    btn24.grid(column=6, row=4)

    btn25 = Button(window, text="y",bg="skyBlue", fg="Black",width=3,height=1,font=('Helvetica','20'),command=lambda: clicked("y"))
    btn25.grid(column=4, row=5)
    btn25 = Button(window, text="z",bg="skyBlue", fg="Black",width=3,height=1,font=('Helvetica','20'),command=lambda: clicked("z"))
    btn25.grid(column=5, row=5)

start()
keyboard()

window.mainloop()
