import time
from tkinter import *
from PIL import ImageTk, Image
import random
from tkinter import messagebox


#Izveido logu
gameWindow = Tk()
gameWindow.title("Attēli")
count = 0  #Atvērtās rūtiņas
correctAnswers = 0  #Pareizās atbildes
answer = []
answer_dict = {}  #Salīdzina attēlus
answernumb = 0

#Galvenā funkcija
def btnClick (btn,number):
    #Globālie mainīgie
    global count #Skaita, cik rūtiņas atvērtas
    global correctAnswers #Skaita pareizās atbildes
    global answer #Tukšs saraksts ar atbildēm
    global answer_dict #Kas ir piespiests, salīdzinās ar attēliem no saraksta
    global answernumb

    if btn['image']=='pyimage2' and count <2:
        btn['image']=imageList[number]
        count+=1 #Viena rutina atklata
        answer.append(number) #Pievieno pie atbildem
        answer_dict[btn]=imageList[number]
    if len(answer)==2: #Ja atvertas divas kartites
        if imageList[answer[0]]==imageList[answer[1]]: #Salīdzina attēlus, kuri saglabāti
            for key in answer_dict:
                key['state']=DISABLED
            correctAnswers+=2
            if correctAnswers==2:
                messagebox.showinfo('Vienādi attēli', 'Esi uzminējis')
                correctAnswers=0
            answernumb+=1
        else:
            Tk.update(btn) #Messagebox update, tapec vajag piespiest programmu updatetot
            time.sleep(0.5)
            messagebox.showinfo('Vienādi attēli', 'Neuzminēji')
            for key in answer_dict:
                key['image']='pyimage2'
        count=0
        answer=[]
        answer_dict={}
        if answernumb==5:

            messagebox.showinfo('Vienādi attēli', 'Malacis! Tu uzvarēji!')
            MsgBox = messagebox.askquestion('Jauna spele','Vai vēlatues sākt jaunu spēli?', icon = 'question')
            #Izveido jautājumu spēles beigās
            if MsgBox == 'yes': #Ja jā, tad reset
                reset()
            else: #Citādi iziet
                quit()
        return 0

def reset():
    global count
    global correctAnswers
    global answer
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

    random.shuffle(imageList) #Saujauc nejaušā secībā
    count = 0
    answer=[]
    answer_dict = {}
    answernumb = 0
    return 0

def infoLogs():
    jaunsLogs=Toplevel()
    jaunsLogs.title('Info par programmu')
    jaunsLogs.geometry('600x200')
    apraksts=Label(jaunsLogs,text='SPĒLES NOTEIKUMI')
    apraksts.grid(row=0,column=0)
    apraksts=Label(jaunsLogs,text='Uz katras kārts ir attēls.')
    apraksts.grid(row=1,column=0)
    apraksts=Label(jaunsLogs,text='Jebkurām divām kārtīm ir tieši viens kopīgs attēls.')
    apraksts.grid(row=2,column=0)
    apraksts=Label(jaunsLogs,text='Pirmais spēlētājs sāk spēli, apgriežot otrādi divas kartiņas. Var arī spēlēt viens, mēģinot atminēt kārtis ar vismazāk mēģinājumiem.')
    apraksts.grid(row=3,column=0)
    apraksts=Label(jaunsLogs,text='Ja apgrieztie attēli ir vienādi, spēlētājs patur sev šo pāri un apgriež otrādi vēl divas kartiņas. ')
    apraksts.grid(row=4,column=0)
    apraksts=Label(jaunsLogs,text='Tā turpinās, kamēr divas apgrieztās kartiņas nesastāda vienādu attēlu pāri.')
    apraksts.grid(row=5,column=0)
    apraksts=Label(jaunsLogs,text='Tad šīs dažādās kartiņas tiek apgrieztas atpakaļ, un spēli turpina nākošais spēlētājs. ')
    apraksts.grid(row=6,column=0)
    apraksts=Label(jaunsLogs,text='Spēle beidzas, kad no galda ir noņemts pēdējais pāris. Spēlētājs, kuram ir visvairāk pāru, ir uzvarētājs.')
    apraksts.grid(row=6,column=0)
    return 0


backgroundImg=ImageTk.PhotoImage(Image.open('UNOback.png')) #Fona attēls
bgImg = ImageTk.PhotoImage(Image.open("UNOback.png").resize((200, 300), Image.Resampling.LANCZOS))

#Definē pogas
btn0 = Button(gameWindow, width=200, height=300, image=bgImg, command=lambda: btnClick(btn0,0))
btn1 = Button(gameWindow, width=200, height=300, image=bgImg, command=lambda: btnClick(btn1,1))
btn2 = Button(gameWindow, width=200, height=300, image=bgImg, command=lambda: btnClick(btn2,2))
btn3 = Button(gameWindow, width=200, height=300, image=bgImg, command=lambda: btnClick(btn3,3))
btn4 = Button(gameWindow, width=200, height=300, image=bgImg, command=lambda: btnClick(btn4,4))
btn5 = Button(gameWindow, width=200, height=300, image=bgImg, command=lambda: btnClick(btn5,5))
btn6 = Button(gameWindow, width=200, height=300, image=bgImg, command=lambda: btnClick(btn6,6))
btn7 = Button(gameWindow, width=200, height=300, image=bgImg, command=lambda: btnClick(btn7,7))
btn8 = Button(gameWindow, width=200, height=300, image=bgImg, command=lambda: btnClick(btn8,8))
btn9 = Button(gameWindow, width=200, height=300, image=bgImg, command=lambda: btnClick(btn9,9))

#Attēli
myImg1=ImageTk.PhotoImage(Image.open('UNOdaudz.jpg').resize((200, 300), Image.Resampling.LANCZOS))
myImg2=ImageTk.PhotoImage(Image.open('UNOzaļš.png').resize((200, 300), Image.Resampling.LANCZOS))
myImg3=ImageTk.PhotoImage(Image.open('UNOsarkans.png').resize((200, 300), Image.Resampling.LANCZOS))
myImg4=ImageTk.PhotoImage(Image.open('UNOdzeltens.png').resize((200, 300), Image.Resampling.LANCZOS))
myImg5=ImageTk.PhotoImage(Image.open('UNOzils.png').resize((200, 300), Image.Resampling.LANCZOS))


#Lielā izvelne
galvenaizvelne=Menu(gameWindow) #Izveido galveno izvelni
gameWindow.config(menu=galvenaizvelne) #Pievieno galvenajam logam

#Mazā izvelne
opcijas=Menu(galvenaizvelne,tearoff=False)
galvenaizvelne.add_cascade(label='Opcijas',menu=opcijas) #Lejupkritosais saraksts

#Komandas
opcijas.add_command(label="Jauna spēle",command=reset)
opcijas.add_command(label="Iziet",command=gameWindow.quit)

galvenaizvelne.add_command(label='Spēles noteikumi',command=infoLogs) #Pievieno mazajai izvelnei

#Attēlu salikšana nejaušā secībā
imageList = [myImg1, myImg1, myImg2, myImg2, myImg3, myImg3, myImg4, myImg4, myImg5, myImg5]
random.shuffle(imageList)

#Pogu atrašanās vietas
btn0.grid(row=0, column=0)
btn1.grid(row=0, column=1)
btn2.grid(row=0, column=2)
btn3.grid(row=0, column=3)
btn4.grid(row=0, column=4)
btn5.grid(row=1, column=0)
btn6.grid(row=1, column=1)
btn7.grid(row=1, column=2)
btn8.grid(row=1, column=3)
btn9.grid(row=1, column=4)


gameWindow.mainloop()
