#tkinter ievietošana
from tkinter import*
from ctypes import resize
from PIL import ImageTk, Image
import random
from tkinter import messagebox


gameWindow=Tk()
gameWindow.title("Attēli")

#Ievieto fotogrāfijas
myImg1=ImageTk.PhotoImage(Image.open("UNOdaudz.jpg"))
myImg2=ImageTk.PhotoImage(Image.open("UNOzils.png"))
myImg3=ImageTk.PhotoImage(Image.open("UNOsarkans.png"))
myImg4=ImageTk.PhotoImage(Image.open("UNOdzeltens.png"))
myImg5=ImageTk.PhotoImage(Image.open("UNOzaļš.png"))

#fona attēls
bgImg=ImageTk.PhotoImage(Image.open("UNOback.png").resize((200,300),Image.Resampling.LANCZOS))

imageList=(myImg1,myImg1,myImg2,myImg2,myImg3,myImg3,myImg4,myImg4,myImg5,myImg5)

random.shuffle(imageList) #sajauc nejaušā secībā

#pogu definēšana un izmērs
btn0=Button(width=200, height=300, image=bgImg)
btn1=Button(width=200, height=300, image=bgImg)
btn2=Button(width=200, height=300, image=bgImg)
btn3=Button(width=200, height=300, image=bgImg)
btn4=Button(width=200, height=300, image=bgImg)
btn5=Button(width=200, height=300, image=bgImg)
btn6=Button(width=200, height=300, image=bgImg)
btn7=Button(width=200, height=300, image=bgImg)
btn8=Button(width=200, height=300, image=bgImg)
btn9=Button(width=200, height=300, image=bgImg)

#pogu atrašanās vieta
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



#logu izveide
gameWindow.mainloop()