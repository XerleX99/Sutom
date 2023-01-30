import tkinter as tk
from tkinter import ttk
import pandas as pd

window = tk.Tk()

dico1 = {}
dico2 = {}


window.bind('<Escape>',lambda e: window.destroy())
window.title("Sutom Solver")

window.attributes('-topmost', True)


window.geometry("650x560")
lettres = ["a","b","c","d","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
numbers10str = ["1","2","3","4","5","6","7","8","9","10"]
numbers10 = [1,2,3,4,5,6,7,8,9,10]
numbers3 = [1,2,3]
numbers26 = [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26]

spbox1 = ttk.Combobox(window,values=lettres,width=2)
spbox2 = ttk.Combobox(window,values=lettres,width=2)
spbox3 = ttk.Combobox(window,values=lettres,width=2)
spbox4 = ttk.Combobox(window,values=lettres,width=2)
spbox5 = ttk.Combobox(window,values=lettres,width=2)
spbox6 = ttk.Combobox(window,values=lettres,width=2)
spbox7 = ttk.Combobox(window,values=lettres,width=2)
spbox8 = ttk.Combobox(window,values=lettres,width=2)
spbox9 = ttk.Combobox(window,values=lettres,width=2)
spbox10 = ttk.Combobox(window,values=lettres,width=2)
spbox11 = ttk.Combobox(window,values=lettres,width=2)
spbox12 = ttk.Combobox(window,values=lettres,width=2)
spbox13 = ttk.Combobox(window,values=lettres,width=2)
spbox14 = ttk.Combobox(window,values=numbers3,width=2)
spbox15 = ttk.Combobox(window,values=numbers3,width=2)
spbox16 = ttk.Combobox(window,values=numbers3,width=2)


entry1 = tk.Entry(window,width=6)
entry2 = tk.Entry(window,width=6)
entry3 = tk.Entry(window,width=6)
entry4 = tk.Entry(window,width=6)
entry5 = tk.Entry(window,width=6)
entry6 = tk.Entry(window,width=6)
entry7 = tk.Entry(window,width=6)
entry8 = tk.Entry(window,width=6)
entry9 = tk.Entry(window,width=6)
entry10 = tk.Entry(window,width=6)


ListSpBox = [spbox1,spbox2,spbox3,spbox4,spbox5,spbox6,spbox7,spbox8,spbox9,spbox10]
ListEntry = [entry1,entry2,entry3,entry4,entry5,entry6,entry7,entry8,entry9,entry10]
ListSpBox2 = [spbox11,spbox12,spbox13]
ListSpBox3 = [spbox14,spbox15,spbox16]

def LetterPos():
  global numletword
  global numletwordint
  numletword = example.get()
  if numletword in numbers10str :
    numletwordint = int(numletword)
    if numletwordint in numbers10 :
      xsp = 3
      ysp = 50
      xent = 3
      yent = 100
      for i in range(0,numletwordint) :
        ListSpBox[i].place(x=xsp,y=ysp)
        ListEntry[i].place(x=xent,y=yent)
        xsp += 50
        xent += 50
      for i in range (numletwordint,10):
        ListSpBox[i].place_forget()
        ListEntry[i].place_forget()

def buttons(bouton : tk.Button):
  if bouton.config('relief')[-1] == 'sunken':
    bouton.config(relief='raised')
  else:
    bouton.config(relief='sunken')

def validate():
  numtemp = spbox11.get()
  xval = 450
  yval = 150
  yval2 = 175
  tk.Label( window, text='lettre en double (ou plus) :').place(x=300,y=150)
  tk.Label( window, text='nombre occurence :').place(x=300,y=175)
  for i in range(0,int(numtemp)):
    ListSpBox2[i].place(x=xval,y=yval)
    ListSpBox3[i].place(x=xval,y=yval2)
    xval += 40
  for i in range (int(numtemp),3):
    ListSpBox2[i].place_forget()
    ListSpBox3[i].place_forget()




def LconBienPlace(data,motEligible1 : list):
  global numletwordint
  global dico1
  for i in range (0,numletwordint):
    dico1[i] = ListSpBox[i].get()
  for word in data["word"] :
      keep = True
      for j in dico1 :
        if dico1[j] in lettres :
          if word[j] != dico1[j] :
              keep = False
              break
      if keep :
          motEligible1.append(word)
    
def LconMalPLace(motEligible1 : list, motEligible2 : list): #TODO vérifier que les lettres mal placer sont comprises dans le mot
  global numletwordint
  global dico2
  for i in range (0,numletwordint):
    dico2[i] = ListEntry[i].get()
  for word in motEligible1 :
    keep = True
    for i in range(0,len(word)):
      for j in dico2[i]:
        if j == word[i]:
          keep = False
    if keep :
      motEligible2.append(word)

def getbadlet():
  btndown = []
  for btn in ListBoutonLettre :
    if btn.config('relief')[-1] == 'sunken' :
      btndown.append(btn['text'].lower())
  return btndown

def LconImpossible(motEligible2 : list, motEligible3 : list):
  letImpo = getbadlet()
  print('letimpo :',letImpo)
  for word in motEligible2 :
    keep = True
    for let in letImpo:
      if word.count(let) > 0 :
        keep = False
    if keep :
      motEligible3.append(word)


def search():
  motEligible1 = []
  motEligible2 = []
  motEligible3 = []
  goodlettres = []
  semigoodlettres = []
  badlettres = []
  data = openfile()
  LconBienPlace(data,motEligible1)
  LconMalPLace(motEligible1,motEligible2)
  LconImpossible(motEligible2,motEligible3)
  print('list mot 1 :',motEligible1)
  print('list mot 2 :',motEligible2)
  print('list mot 3 :',motEligible3)
  x = ', '.join(motEligible3)
  Resultlab.config(text=x)
  

def openfile():
  Flettre = spbox1.get()
  classer = str (Flettre)+(" classed.xlsx")
  page = str (Flettre)+(" words")+str(numletword)
  df = pd.read_excel(classer,str(page))
  return df



tk.Label(window,text="Nombre de lettre du mot :").place(x = 0,y= 5)

example = ttk.Combobox(window,values=numbers10,width=2)
example.place(x=150,y=5)

tk.Button(window,text="OK",command=LetterPos,width=2).place(x=200,y=2)

tk.Label(window,text="Entrer les bonnes lettres :").place(x = 0, y = 25)

tk.Label(window,text="Entrer les lettres mal placés aux endroits où on sais qu'elle ne peuvent pas être (séparées d'une virgule) :").place(x=0,y=75)

tk.Label(window,text="Selectionner les lettres impossibles :").place(x=0,y=125)

btnA = tk.Button(window,text='A',command=lambda:buttons(btnA),relief='raised',width=1,height=1)
btnA.place(x=5,y=160)
btnZ = tk.Button(window,text='Z',command=lambda:buttons(btnZ),relief='raised',width=1,height=1)
btnZ.place(x=30,y=160)
btnE = tk.Button(window,text='E',command=lambda:buttons(btnE),relief='raised',width=1,height=1)
btnE.place(x=55,y=160)
btnR = tk.Button(window,text='R',command=lambda:buttons(btnR),relief='raised',width=1,height=1)
btnR.place(x=80,y=160)
btnT = tk.Button(window,text='T',command=lambda:buttons(btnT),relief='raised',width=1,height=1)
btnT.place(x=105,y=160)
btnY = tk.Button(window,text='Y',command=lambda:buttons(btnY),relief='raised',width=1,height=1)
btnY.place(x=130,y=160)
btnU = tk.Button(window,text='U',command=lambda:buttons(btnU),relief='raised',width=1,height=1)
btnU.place(x=155,y=160)
btnI = tk.Button(window,text='I',command=lambda:buttons(btnI),relief='raised',width=1,height=1)
btnI.place(x=180,y=160)
btnO = tk.Button(window,text='O',command=lambda:buttons(btnO),relief='raised',width=1,height=1)
btnO.place(x=205,y=160)
btnP = tk.Button(window,text='P',command=lambda:buttons(btnP),relief='raised',width=1,height=1)
btnP.place(x=230,y=160)
btnQ = tk.Button(window,text='Q',command=lambda:buttons(btnQ),relief='raised',width=1,height=1)
btnQ.place(x=10,y=195)
btnS = tk.Button(window,text='S',command=lambda:buttons(btnS),relief='raised',width=1,height=1)
btnS.place(x=35,y=195)
btnD = tk.Button(window,text='D',command=lambda:buttons(btnD),relief='raised',width=1,height=1)
btnD.place(x=60,y=195)
btnF = tk.Button(window,text='F',command=lambda:buttons(btnF),relief='raised',width=1,height=1)
btnF.place(x=85,y=195)
btnG = tk.Button(window,text='G',command=lambda:buttons(btnG),relief='raised',width=1,height=1)
btnG.place(x=110,y=195)
btnH = tk.Button(window,text='H',command=lambda:buttons(btnH),relief='raised',width=1,height=1)
btnH.place(x=135,y=195)
btnJ = tk.Button(window,text='J',command=lambda:buttons(btnJ),relief='raised',width=1,height=1)
btnJ.place(x=160,y=195)
btnK = tk.Button(window,text='K',command=lambda:buttons(btnK),relief='raised',width=1,height=1)
btnK.place(x=185,y=195)
btnL = tk.Button(window,text='L',command=lambda:buttons(btnL),relief='raised',width=1,height=1)
btnL.place(x=210,y=195)
btnM = tk.Button(window,text='M',command=lambda:buttons(btnM),relief='raised',width=1,height=1)
btnM.place(x=235,y=195)
btnW = tk.Button(window,text='W',command=lambda:buttons(btnW),relief='raised',width=1,height=1)
btnW.place(x=50,y=230)
btnX = tk.Button(window,text='X',command=lambda:buttons(btnX),relief='raised',width=1,height=1)
btnX.place(x=75,y=230)
btnC = tk.Button(window,text='C',command=lambda:buttons(btnC),relief='raised',width=1,height=1)
btnC.place(x=100,y=230)
btnV = tk.Button(window,text='V',command=lambda:buttons(btnV),relief='raised',width=1,height=1)
btnV.place(x=125,y=230)
btnB = tk.Button(window,text='B',command=lambda:buttons(btnB),relief='raised',width=1,height=1)
btnB.place(x=150,y=230)
btnN = tk.Button(window,text='N',command=lambda:buttons(btnN),relief='raised',width=1,height=1)
btnN.place(x=175,y=230)

ListBoutonLettre = [btnA,btnZ,btnE,btnR,btnT,btnY,btnU,btnI,btnO,btnP,btnQ,btnS,btnD,btnF,btnG,btnH,btnJ,btnK,btnL,btnM,btnW,btnX,btnC,btnV,btnB,btnN]

tk.Label( window, text='Nombre de lettre en double (ou plus) :').place(x=300,y=125)

multipleLettres = [1,2,3]
spbox11 = ttk.Combobox(window,values=multipleLettres,width=2)
spbox11.place(x=515,y=125)

tk.Button(window,text='validate',command=validate).place(x=555,y=122)

tk.Button(window,text='Search',command=search,width=10,height=3).place(x=450,y=240)

tk.Label( window, text='Possible solution of the word : ').place(x=5,y=290)



Resultlab = tk.Label( window, text="",width=90,height=15,relief='ridge',wraplengt=600)
Resultlab.place(x=5,y=320)



window.mainloop()