import tkinter as tk
from tkinter import ttk


window = tk.Tk()


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


def LetterPos():
    numletword = example.get()
    if numletword in numbers10str :
      numletword = int(numletword)
      if numletword in numbers10 :
          
          if numletword == 1 :
              spbox1.place(x=0,y= 50)
              spbox2.place_forget()
              spbox3.place_forget()
              spbox4.place_forget()
              spbox5.place_forget()
              spbox6.place_forget()
              spbox7.place_forget()
              spbox8.place_forget()
              spbox9.place_forget()
              spbox10.place_forget()
              
              entry1.place(x=0,y=100)
              entry2.place_forget()
              entry3.place_forget()
              entry4.place_forget()
              entry5.place_forget()
              entry6.place_forget()
              entry7.place_forget()
              entry8.place_forget()
              entry9.place_forget()
              entry10.place_forget()
              
          elif numletword == 2 :
              spbox1.place(x=0,y= 50)
              spbox2.place(x=150,y= 50)
              spbox3.place_forget()
              spbox4.place_forget()
              spbox5.place_forget()
              spbox6.place_forget()
              spbox7.place_forget()
              spbox8.place_forget()
              spbox9.place_forget()
              spbox10.place_forget()
              
              entry1.place(x=7,y= 100)
              entry2.place(x=157,y= 100)
              entry3.place_forget()
              entry4.place_forget()
              entry5.place_forget()
              entry6.place_forget()
              entry7.place_forget()
              entry8.place_forget()
              entry9.place_forget()
              entry10.place_forget()
          elif numletword == 3 :
              spbox1.place(x=0,y= 50)
              spbox2.place(x=150,y= 50)
              spbox3.place(x=300,y= 50)
              spbox4.place_forget()
              spbox5.place_forget()
              spbox6.place_forget()
              spbox7.place_forget()
              spbox8.place_forget()
              spbox9.place_forget()
              spbox10.place_forget()
              
              entry1.place(x=7,y= 100)
              entry2.place(x=157,y= 100)
              entry3.place(x=307,y= 100)
              entry4.place_forget()
              entry5.place_forget()
              entry6.place_forget()
              entry7.place_forget()
              entry8.place_forget()
              entry9.place_forget()
              entry10.place_forget()
          elif numletword == 4 :
              spbox1.place(x=0,y= 50)
              spbox2.place(x=150,y= 50)
              spbox3.place(x=300,y= 50)
              spbox4.place(x=450,y= 50)
              spbox5.place_forget()
              spbox6.place_forget()
              spbox7.place_forget()
              spbox8.place_forget()
              spbox9.place_forget()
              spbox10.place_forget()
              
              entry1.place(x=7,y= 100)
              entry2.place(x=157,y= 100)
              entry3.place(x=307,y= 100)
              entry4.place(x=457,y= 100)
              entry5.place_forget()
              entry6.place_forget()
              entry7.place_forget()
              entry8.place_forget()
              entry9.place_forget()
              entry10.place_forget()
              
          elif numletword == 5 :
              spbox1.place(x=0,y= 50)
              spbox2.place(x=150,y= 50)
              spbox3.place(x=300,y= 50)
              spbox4.place(x=450,y= 50)
              spbox5.place(x=600,y= 50)
              spbox6.place_forget()
              spbox7.place_forget()
              spbox8.place_forget()
              spbox9.place_forget()
              spbox10.place_forget()
              
              entry1.place(x=7,y= 100)
              entry2.place(x=157,y= 100)
              entry3.place(x=307,y= 100)
              entry4.place(x=457,y= 100)
              entry5.place(x=607,y= 100)
              entry6.place_forget()
              entry7.place_forget()
              entry8.place_forget()
              entry9.place_forget()
              entry10.place_forget()
          elif numletword == 6 :
              spbox1.place(x=0,y= 50)
              spbox2.place(x=150,y= 50)
              spbox3.place(x=300,y= 50)
              spbox4.place(x=450,y= 50)
              spbox5.place(x=600,y= 50)
              spbox6.place(x=750,y= 50)
              spbox7.place_forget()
              spbox8.place_forget()
              spbox9.place_forget()
              spbox10.place_forget()
              
              entry1.place(x=7,y= 100)
              entry2.place(x=157,y= 100)
              entry3.place(x=307,y= 100)
              entry4.place(x=457,y= 100)
              entry5.place(x=607,y= 100)
              entry6.place(x=757,y= 100)
              entry7.place_forget()
              entry8.place_forget()
              entry9.place_forget()
              entry10.place_forget()
          elif numletword == 7:
              spbox1.place(x=0,y= 50)
              spbox2.place(x=150,y= 50)
              spbox3.place(x=300,y= 50)
              spbox4.place(x=450,y= 50)
              spbox5.place(x=600,y= 50)
              spbox6.place(x=750,y= 50)
              spbox7.place(x=900,y= 50)
              spbox8.place_forget()
              spbox9.place_forget()
              spbox10.place_forget()
              
              entry1.place(x=7,y= 100)
              entry2.place(x=157,y= 100)
              entry3.place(x=307,y= 100)
              entry4.place(x=457,y= 100)
              entry5.place(x=607,y= 100)
              entry6.place(x=757,y= 100)
              entry7.place(x=907,y= 100)
              entry8.place_forget()
              entry9.place_forget()
              entry10.place_forget()
          elif numletword == 8 :
              spbox1.place(x=0,y= 50)
              spbox2.place(x=150,y= 50)
              spbox3.place(x=300,y= 50)
              spbox4.place(x=450,y= 50)
              spbox5.place(x=600,y= 50)
              spbox6.place(x=750,y= 50)
              spbox7.place(x=900,y= 50)
              spbox8.place(x=1050,y= 50)
              spbox9.place_forget()
              spbox10.place_forget()
              
              entry1.place(x=7,y= 100)
              entry2.place(x=157,y= 100)
              entry3.place(x=307,y= 100)
              entry4.place(x=457,y= 100)
              entry5.place(x=607,y= 100)
              entry6.place(x=757,y= 100)
              entry7.place(x=907,y= 100)
              entry8.place(x=1057,y= 100)
              entry9.place_forget()
              entry10.place_forget()
          elif numletword == 9 :
              spbox1.place(x=0,y= 50)
              spbox2.place(x=150,y= 50)
              spbox3.place(x=300,y= 50)
              spbox4.place(x=450,y= 50)
              spbox5.place(x=600,y= 50)
              spbox6.place(x=750,y= 50)
              spbox7.place(x=900,y= 50)
              spbox8.place(x=1050,y= 50)
              spbox9.place(x=1200,y= 50)
              spbox10.place_forget()
              
              entry1.place(x=7,y= 100)
              entry2.place(x=157,y= 100)
              entry3.place(x=307,y= 100)
              entry4.place(x=457,y= 100)
              entry5.place(x=607,y= 100)
              entry6.place(x=757,y= 100)
              entry7.place(x=907,y= 100)
              entry8.place(x=1057,y= 100)
              entry9.place(x=1207,y= 100)
              entry10.place_forget()
          elif numletword == 10 :
              spbox1.place(x=0,y= 50)
              spbox2.place(x=150,y= 50)
              spbox3.place(x=300,y= 50)
              spbox4.place(x=450,y= 50)
              spbox5.place(x=600,y= 50)
              spbox6.place(x=750,y= 50)
              spbox7.place(x=900,y= 50)
              spbox8.place(x=1050,y= 50)
              spbox9.place(x=1200,y= 50)
              spbox10.place(x=1350,y= 50)
              
              entry1.place(x=7,y= 100)
              entry2.place(x=157,y= 100)
              entry3.place(x=307,y= 100)
              entry4.place(x=457,y= 100)
              entry5.place(x=607,y= 100)
              entry6.place(x=757,y= 100)
              entry7.place(x=907,y= 100)
              entry8.place(x=1057,y= 100)
              entry9.place(x=1207,y= 100)
              entry10.place(x=1357,y= 100)

def A():    
  if btnA.config('relief')[-1] == 'sunken':
    btnA.config(relief='raised')
  else:
    btnA.config(relief='sunken')
def B():
  if btnB.config('relief')[-1] == 'sunken':
    btnB.config(relief='raised')
  else:
    btnB.config(relief='sunken')
def C():
  if btnC.config('relief')[-1] == 'sunken':
    btnC.config(relief='raised')
  else:
    btnC.config(relief='sunken')
def D():
  if btnD.config('relief')[-1] == 'sunken':
    btnD.config(relief='raised')
  else:
    btnD.config(relief='sunken')
def E():
  if btnE.config('relief')[-1] == 'sunken':
    btnE.config(relief='raised')
  else:
    btnE.config(relief='sunken')
def F():
  if btnF.config('relief')[-1] == 'sunken':
    btnF.config(relief='raised')
  else:
    btnF.config(relief='sunken')
def G():
  if btnG.config('relief')[-1] == 'sunken':
    btnG.config(relief='raised')
  else:
    btnG.config(relief='sunken')
def H():
  if btnH.config('relief')[-1] == 'sunken':
    btnH.config(relief='raised')
  else:
    btnH.config(relief='sunken')
def I():
  if btnI.config('relief')[-1] == 'sunken':
    btnI.config(relief='raised')
  else:
    btnI.config(relief='sunken')
def J():
  if btnJ.config('relief')[-1] == 'sunken':
    btnJ.config(relief='raised')
  else:
    btnJ.config(relief='sunken')
def K():
  if btnK.config('relief')[-1] == 'sunken':
    btnK.config(relief='raised')
  else:
    btnK.config(relief='sunken')
def L():
  if btnL.config('relief')[-1] == 'sunken':
    btnL.config(relief='raised')
  else:
    btnL.config(relief='sunken')
def M():
  if btnM.config('relief')[-1] == 'sunken':
    btnM.config(relief='raised')
  else:
    btnM.config(relief='sunken')
def N():
  if btnN.config('relief')[-1] == 'sunken':
    btnN.config(relief='raised')
  else:
    btnN.config(relief='sunken')
def O():
  if btnO.config('relief')[-1] == 'sunken':
    btnO.config(relief='raised')
  else:
    btnO.config(relief='sunken')
def P():
  if btnP.config('relief')[-1] == 'sunken':
    btnP.config(relief='raised')
  else:
    btnP.config(relief='sunken')
def Q():
  if btnQ.config('relief')[-1] == 'sunken':
    btnQ.config(relief='raised')
  else:
    btnQ.config(relief='sunken')
def R():
  if btnR.config('relief')[-1] == 'sunken':
    btnR.config(relief='raised')
  else:
    btnR.config(relief='sunken')
def S():
  if btnS.config('relief')[-1] == 'sunken':
    btnS.config(relief='raised')
  else:
    btnS.config(relief='sunken')
def T():
  if btnT.config('relief')[-1] == 'sunken':
    btnT.config(relief='raised')
  else:
    btnT.config(relief='sunken')
def U():
  if btnU.config('relief')[-1] == 'sunken':
    btnU.config(relief='raised')
  else:
    btnU.config(relief='sunken')
def V():
  if btnV.config('relief')[-1] == 'sunken':
    btnV.config(relief='raised')
  else:
    btnV.config(relief='sunken')
def W():
  if btnW.config('relief')[-1] == 'sunken':
    btnW.config(relief='raised')
  else:
    btnW.config(relief='sunken')
def X():
  if btnX.config('relief')[-1] == 'sunken':
    btnX.config(relief='raised')
  else:
    btnX.config(relief='sunken')
def Y():
  if btnY.config('relief')[-1] == 'sunken':
    btnY.config(relief='raised')
  else:
    btnY.config(relief='sunken')
def Z():
  if btnZ.config('relief')[-1] == 'sunken':
    btnZ.config(relief='raised')
  else:
    btnZ.config(relief='sunken')
            
def search():
  pass

tk.Label(window,text="Nombre de lettre du mot :").place(x = 0,y= 5)

example = ttk.Combobox(window,values=numbers10)
example.place(x=150,y=5)

tk.Button(window,text="OK",command=LetterPos).place(x=300,y=2)

tk.Label(window,text="Entrer les bonnes lettres :").place(x = 0, y = 25)

tk.Label(window,text="Entrer les lettres mal placés aux endroits où on sais qu'elle ne peuvent pas être (séparées d'une virgule) :").place(x=0,y=75)

tk.Label(window,text="Selectionner les lettres impossibles :").place(x=0,y=125)

btnA = tk.Button(window,text='A',command=A,relief='raised',width=1,height=1)
btnA.place(x=30,y=175)
btnZ = tk.Button(window,text='Z',command=Z,relief='raised',width=1,height=1)
btnZ.place(x=55,y=175)
btnE = tk.Button(window,text='E',command=E,relief='raised',width=1,height=1)
btnE.place(x=80,y=175)
btnR = tk.Button(window,text='R',command=R,relief='raised',width=1,height=1)
btnR.place(x=105,y=175)
btnT = tk.Button(window,text='T',command=T,relief='raised',width=1,height=1)
btnT.place(x=130,y=175)
btnY = tk.Button(window,text='Y',command=Y,relief='raised',width=1,height=1)
btnY.place(x=155,y=175)
btnU = tk.Button(window,text='U',command=U,relief='raised',width=1,height=1)
btnU.place(x=180,y=175)
btnI = tk.Button(window,text='I',command=I,relief='raised',width=1,height=1)
btnI.place(x=205,y=175)
btnO = tk.Button(window,text='O',command=O,relief='raised',width=1,height=1)
btnO.place(x=230,y=175)
btnP = tk.Button(window,text='P',command=P,relief='raised',width=1,height=1)
btnP.place(x=255,y=175)
btnQ = tk.Button(window,text='Q',command=Q,relief='raised',width=1,height=1)
btnQ.place(x=35,y=210)
btnS = tk.Button(window,text='S',command=S,relief='raised',width=1,height=1)
btnS.place(x=60,y=210)
btnD = tk.Button(window,text='D',command=D,relief='raised',width=1,height=1)
btnD.place(x=85,y=210)
btnF = tk.Button(window,text='F',command=F,relief='raised',width=1,height=1)
btnF.place(x=110,y=210)
btnG = tk.Button(window,text='G',command=G,relief='raised',width=1,height=1)
btnG.place(x=135,y=210)
btnH = tk.Button(window,text='H',command=H,relief='raised',width=1,height=1)
btnH.place(x=160,y=210)
btnJ = tk.Button(window,text='J',command=J,relief='raised',width=1,height=1)
btnJ.place(x=185,y=210)
btnK = tk.Button(window,text='K',command=K,relief='raised',width=1,height=1)
btnK.place(x=210,y=210)
btnL = tk.Button(window,text='L',command=L,relief='raised',width=1,height=1)
btnL.place(x=235,y=210)
btnM = tk.Button(window,text='M',command=M,relief='raised',width=1,height=1)
btnM.place(x=260,y=210)
btnW = tk.Button(window,text='W',command=W,relief='raised',width=1,height=1)
btnW.place(x=75,y=245)
btnX = tk.Button(window,text='X',command=X,relief='raised',width=1,height=1)
btnX.place(x=100,y=245)
btnC = tk.Button(window,text='C',command=C,relief='raised',width=1,height=1)
btnC.place(x=125,y=245)
btnV = tk.Button(window,text='V',command=V,relief='raised',width=1,height=1)
btnV.place(x=150,y=245)
btnB = tk.Button(window,text='B',command=B,relief='raised',width=1,height=1)
btnB.place(x=175,y=245)
btnN = tk.Button(window,text='N',command=N,relief='raised',width=1,height=1)
btnN.place(x=200,y=245)

tk.Button(window,text='Search',command=search).place(x=330,y=260)

tk.Label( window, text='Possible solution of the word : ').place(x=5,y=290)


var = tk.StringVar()
var =""
Resultlab = tk.Label( window, text=var,width=60,height=15,relief='ridge')
Resultlab.place(x=5,y=320)

window.mainloop()