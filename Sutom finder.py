import pandas as pd
import time
import os

os.chdir(os.path.dirname(os.path.abspath(__file__)))


def LconBienPlace(couples : list):
    for word in df["word"] :
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


Flettre = input("Première lettre du mot (en minuscul) : \n")
Nlettre = int(input("Nombre de lettre du mot : \n"))

classer = str (Flettre)+(" classed.xlsx")
page = str (Flettre)+(" words")+str(Nlettre)
df = pd.read_excel(classer,str(page))

motEligible1 = []
motEligible2 = []
motEligible3 = []
goodlettres = []
semigoodlettres = []
badlettres = []

nb = int(input("nombre de lettre bien placées : \n"))
for i in range(0,nb):
    goodlettres.append((input("lettre_bien_placée position : \n").split()))

nmp = int(input("nombre de lettre mal placées : \n"))
for i in range(0,nmp):
    semigoodlettres.append((input("lettre_mal_placée position_impossible nombre_de_fois_présente_minimum: \n").split()))

ni = int(input("nombre de lettre impossible : \n"))
for i in range(0,ni):
    badlettres.append((input("lettre impossible : \n")))


LconBienPlace(goodlettres)
# print("good lettre filtred : ",motEligible1)
LconMalPLace(semigoodlettres)
# print("semi good lettre filtred :",motEligible1)
LconImpossible(badlettres)
# print("bad lettre filtred")

print(motEligible3)


input("presse enter to close")        