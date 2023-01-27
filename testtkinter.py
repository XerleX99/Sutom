import tkinter as tk
from tkinter import ttk
import pandas as pd


window = tk.Tk()

numletword = tk.StringVar()
var = tk.StringVar()

window.bind('<Escape>',lambda e: window.destroy())



window.geometry("1400x600")
lettres = ["a","b","c","d","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
numbers10str = ["1","2","3","4","5","6","7","8","9","10"]
numbers10 = [1,2,3,4,5,6,7,8,9,10]
numbers26 = [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26]

spbox1 = ttk.Combobox(window,values=lettres)
spbox2 = ttk.Combobox(window,values=lettres)
spbox3 = ttk.Combobox(window,values=lettres)
spbox4 = ttk.Combobox(window,values=lettres)
spbox5 = ttk.Combobox(window,values=lettres)
spbox6 = ttk.Combobox(window,values=lettres)
spbox7 = ttk.Combobox(window,values=lettres)
spbox8 = ttk.Combobox(window,values=lettres)
spbox9 = ttk.Combobox(window,values=lettres)
spbox10 = ttk.Combobox(window,values=lettres)

entry1 = tk.Entry(window)
entry2 = tk.Entry(window)
entry3 = tk.Entry(window)
entry4 = tk.Entry(window)
entry5 = tk.Entry(window)
entry6 = tk.Entry(window)
entry7 = tk.Entry(window)
entry8 = tk.Entry(window)
entry9 = tk.Entry(window)
entry10 = tk.Entry(window)

ListSpBox = [spbox1,spbox2,spbox3,spbox4,spbox5,spbox6,spbox7,spbox8,spbox9,spbox10]
ListEntry = [entry1,entry2,entry3,entry4,entry5,entry6,entry7,entry8,entry9,entry10]

def LetterPos():
    numletword = example.get()
    if numletword in numbers10str :
      numletword = int(numletword)
      if numletword in numbers10 :
        xsp = 0
        ysp = 50
        xent = 7
        yent = 100
        for i in range(0,numletword) :
          ListSpBox[i].place(x=xsp,y=ysp)
          ListEntry[i].place(x=xent,y=yent)
          xsp += 150
          xent += 150
        for i in range (numletword,10):
          ListSpBox[i].place_forget()
          ListEntry[i].place_forget()

def buttons(bouton : tk.Button):
  if bouton.config('relief')[-1] == 'sunken':
    bouton.config(relief='raised')
  else:
    bouton.config(relief='sunken')

def LconBienPlace(data,couples : list):
    for word in data["word"] :
        keep = True
        for x,y in couples :
            if word[int(y)-1] != x :
                keep = False
                break
        if keep :
            motEligible1.append(word)
    
def LconMalPLace(couples : list):
    for word in motEligible1 :
        keep = True
        for i,j,k in couples :
            if word.count(i) < int(k) :
                keep = False
            if word[int(j)-1] == i :
                keep = False
        if keep is True :
            motEligible2.append(word)

def LconImpossible(couples : list):
    for word in motEligible2 :
        keep = True
        for l in couples :
            if word.count(l) != 0 :
                keep = False
        if keep is True:
            motEligible3.append(word)
            
def search():
  data = openfile()
  
  motEligible1 = []
  motEligible2 = []
  motEligible3 = []
  goodlettres = []
  semigoodlettres = []
  badlettres = []

def openfile():
  Flettre = spbox1.get()
  classer = str (Flettre)+(" classed.xlsx")
  page = str (Flettre)+(" words")+numletword
  df = pd.read_excel(classer,str(page))
  return df



tk.Label(window,text="Nombre de lettre du mot :").place(x = 0,y= 5)

example = ttk.Combobox(window,values=numbers10)
example.place(x=150,y=5)

tk.Button(window,text="OK",command=LetterPos).place(x=300,y=2)

tk.Label(window,text="Entrer les bonnes lettres :").place(x = 0, y = 25)

tk.Label(window,text="Entrer les lettres mal placés aux endroits où on sais qu'elle ne peuvent pas être (séparées d'une virgule) :").place(x=0,y=75)

tk.Label(window,text="Selectionner les lettres impossibles :").place(x=0,y=125)

btnA = tk.Button(window,text='A',command=lambda:buttons(btnA),relief='raised',width=1,height=1)
btnA.place(x=30,y=175)
btnZ = tk.Button(window,text='Z',command=lambda:buttons(btnZ),relief='raised',width=1,height=1)
btnZ.place(x=55,y=175)
btnE = tk.Button(window,text='E',command=lambda:buttons(btnE),relief='raised',width=1,height=1)
btnE.place(x=80,y=175)
btnR = tk.Button(window,text='R',command=lambda:buttons(btnR),relief='raised',width=1,height=1)
btnR.place(x=105,y=175)
btnT = tk.Button(window,text='T',command=lambda:buttons(btnT),relief='raised',width=1,height=1)
btnT.place(x=130,y=175)
btnY = tk.Button(window,text='Y',command=lambda:buttons(btnY),relief='raised',width=1,height=1)
btnY.place(x=155,y=175)
btnU = tk.Button(window,text='U',command=lambda:buttons(btnU),relief='raised',width=1,height=1)
btnU.place(x=180,y=175)
btnI = tk.Button(window,text='I',command=lambda:buttons(btnI),relief='raised',width=1,height=1)
btnI.place(x=205,y=175)
btnO = tk.Button(window,text='O',command=lambda:buttons(btnO),relief='raised',width=1,height=1)
btnO.place(x=230,y=175)
btnP = tk.Button(window,text='P',command=lambda:buttons(btnP),relief='raised',width=1,height=1)
btnP.place(x=255,y=175)
btnQ = tk.Button(window,text='Q',command=lambda:buttons(btnQ),relief='raised',width=1,height=1)
btnQ.place(x=35,y=210)
btnS = tk.Button(window,text='S',command=lambda:buttons(btnS),relief='raised',width=1,height=1)
btnS.place(x=60,y=210)
btnD = tk.Button(window,text='D',command=lambda:buttons(btnD),relief='raised',width=1,height=1)
btnD.place(x=85,y=210)
btnF = tk.Button(window,text='F',command=lambda:buttons(btnF),relief='raised',width=1,height=1)
btnF.place(x=110,y=210)
btnG = tk.Button(window,text='G',command=lambda:buttons(btnG),relief='raised',width=1,height=1)
btnG.place(x=135,y=210)
btnH = tk.Button(window,text='H',command=lambda:buttons(btnH),relief='raised',width=1,height=1)
btnH.place(x=160,y=210)
btnJ = tk.Button(window,text='J',command=lambda:buttons(btnJ),relief='raised',width=1,height=1)
btnJ.place(x=185,y=210)
btnK = tk.Button(window,text='K',command=lambda:buttons(btnK),relief='raised',width=1,height=1)
btnK.place(x=210,y=210)
btnL = tk.Button(window,text='L',command=lambda:buttons(btnL),relief='raised',width=1,height=1)
btnL.place(x=235,y=210)
btnM = tk.Button(window,text='M',command=lambda:buttons(btnM),relief='raised',width=1,height=1)
btnM.place(x=260,y=210)
btnW = tk.Button(window,text='W',command=lambda:buttons(btnW),relief='raised',width=1,height=1)
btnW.place(x=75,y=245)
btnX = tk.Button(window,text='X',command=lambda:buttons(btnX),relief='raised',width=1,height=1)
btnX.place(x=100,y=245)
btnC = tk.Button(window,text='C',command=lambda:buttons(btnC),relief='raised',width=1,height=1)
btnC.place(x=125,y=245)
btnV = tk.Button(window,text='V',command=lambda:buttons(btnV),relief='raised',width=1,height=1)
btnV.place(x=150,y=245)
btnB = tk.Button(window,text='B',command=lambda:buttons(btnB),relief='raised',width=1,height=1)
btnB.place(x=175,y=245)
btnN = tk.Button(window,text='N',command=lambda:buttons(btnN),relief='raised',width=1,height=1)
btnN.place(x=200,y=245)

tk.Button(window,text='Search',command=search).place(x=330,y=260)

tk.Label( window, text='Possible solution of the word : ').place(x=5,y=290)


var = tk.StringVar()
var =""
Resultlab = tk.Label( window, text=var,width=60,height=15,relief='ridge')
Resultlab.place(x=5,y=320)

window.mainloop()