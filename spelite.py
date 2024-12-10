import time
from tkinter import *
from PIL import ImageTk, Image
import random
from tkinter import messagebox

# Izveido logu
gameWindow = Tk()
gameWindow.title("Attēli")

count = 0  # Atvērtās rūtiņas
correctAnswers = 0  # Pareizās atbildes
answer = []
answer_dict = {}  # Salīdzina attēlus
answernumb = 0

# Galvenā funkcija
def btnClick(btn, number):
    global count
    global correctAnswers
    global answer
    global answer_dict
    global answernumb

    if btn["image"] == "pyImage2" and count < 2:
        btn["image"] = imageList[number]
        count += 1
        answer.append(number)
        answer_dict[btn] = imageList[number]

    if len(answer) == 2:
        if imageList[answer[0]] == imageList[answer[1]]:
            for key in answer_dict:
                key["state"] = DISABLED
            correctAnswers += 2
            if correctAnswers == 2:
                messagebox.showinfo("Vienādi attēli", "Esi uzminējis")
                correctAnswers = 0
            answernumb += 1
        else:
            gameWindow.update()  
            time.sleep(0.5)
            messagebox.showinfo("Vienādi attēli", "Neuzminēji")
            for key in answer_dict:
                key["image"] = "pyImage2"
            count = 0
            answer.clear()
            answer_dict.clear()

    if answernumb == 5:
        messagebox.showinfo("Vienādi attēli", "Malacis! Tu uzvarēji")
        MsgBox = messagebox.askquestion("Jauna spēle", "Vai vēlies sākt spēli?")
        if MsgBox == "yes":
            reset()  
        else:
            gameWindow.quit() 
    

def reset():
    global count
    global correctAnswers
    global answer_dict
    global answernumb

    
    btn0.config(state=NORMAL)
    btn1.config(state=NORMAL)
    btn2.config(state=NORMAL)
    btn3.config(state=NORMAL)
    btn4.config(state=NORMAL)
    btn5.config(state=NORMAL)
    btn6.config(state=NORMAL)
    btn7.config(state=NORMAL)
    btn8.config(state=NORMAL)
    btn9.config(state=NORMAL)

    btn0['image']='pyimage2'
    btn1['image']='pyimage2'
    btn2['image']='pyimage2'
    btn3['image']='pyimage2'
    btn4['image']='pyimage2'
    btn5['image']='pyimage2'
    btn6['image']='pyimage2'
    btn7['image']='pyimage2'
    btn8['image']='pyimage2'
    btn9['image']='pyimage2'

    random.shuffle(imageList)  

    
    count = 0
    correctAnswers = 0
    answer.clear()
    answer_dict.clear()
    answernumb = 0
    return 0

# Attēli
myImg1 = ImageTk.PhotoImage(Image.open("UNOdaudz.jpg"))
myImg2 = ImageTk.PhotoImage(Image.open("UNOzils.png"))
myImg3 = ImageTk.PhotoImage(Image.open("UNOsarkans.png"))
myImg4 = ImageTk.PhotoImage(Image.open("UNOdzeltens.png"))
myImg5 = ImageTk.PhotoImage(Image.open("UNOzaļš.png"))

# Virsējais attēls
bgImg = ImageTk.PhotoImage(Image.open("UNOback.png").resize((200, 300), Image.Resampling.LANCZOS))

# List of images, shuffled
imageList = [myImg1, myImg1, myImg2, myImg2, myImg3, myImg3, myImg4, myImg4, myImg5, myImg5]
random.shuffle(imageList)

# Definē pogas
btn0 = Button(gameWindow, width=200, height=300, image=bgImg, command=lambda: btnClick(btn0, 0))
btn1 = Button(gameWindow, width=200, height=300, image=bgImg, command=lambda: btnClick(btn1, 1))
btn2 = Button(gameWindow, width=200, height=300, image=bgImg, command=lambda: btnClick(btn2, 2))
btn3 = Button(gameWindow, width=200, height=300, image=bgImg, command=lambda: btnClick(btn3, 3))
btn4 = Button(gameWindow, width=200, height=300, image=bgImg, command=lambda: btnClick(btn4, 4))
btn5 = Button(gameWindow, width=200, height=300, image=bgImg, command=lambda: btnClick(btn5, 5))
btn6 = Button(gameWindow, width=200, height=300, image=bgImg, command=lambda: btnClick(btn6, 6))
btn7 = Button(gameWindow, width=200, height=300, image=bgImg, command=lambda: btnClick(btn7, 7))
btn8 = Button(gameWindow, width=200, height=300, image=bgImg, command=lambda: btnClick(btn8, 8))
btn9 = Button(gameWindow, width=200, height=300, image=bgImg, command=lambda: btnClick(btn9, 9))

# Pogu atrašanās vietas
btn0.grid(row=0, column=1)
btn1.grid(row=0, column=2)
btn2.grid(row=0, column=3)
btn3.grid(row=0, column=4)
btn4.grid(row=0, column=5)
btn5.grid(row=1, column=1)
btn6.grid(row=1, column=2)
btn7.grid(row=1, column=3)
btn8.grid(row=1, column=4)
btn9.grid(row=1, column=5)

# Logu izveide
gameWindow.mainloop()
