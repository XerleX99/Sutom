import pandas as pd
import os

os.chdir(os.path.dirname(os.path.abspath(__file__)))



df = pd.read_excel("Lexique383_bis.xlsx")

#print(df.columns)
x,y = df.shape
print("x,y", x, y)
alph = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

for letter in alph :
    print ("\n",letter,"\n")
    
    words1 = []
    words2 = []
    words3 = []
    words4 = []
    words5 = []
    words6 = []
    words7 = []
    words8 = []
    words9 = []
    words = []

    print("classing")

    for i in range (0,x) :
        if str(df['1_ortho'][i][0]) == letter :
            if i%50000 == 0:
                print(i)
            if df['15_nblettres'][i] == 1 :
                words1.append(df['1_ortho'][i])
            elif df['15_nblettres'][i] == 2 :
                words2.append(df['1_ortho'][i])
            elif df['15_nblettres'][i] == 3 :
                words3.append(df['1_ortho'][i])
            elif df['15_nblettres'][i] == 4 :
                words4.append(df['1_ortho'][i])
            elif df['15_nblettres'][i] == 5 :
                words5.append(df['1_ortho'][i])
            elif df['15_nblettres'][i] == 6 :
                words6.append(df['1_ortho'][i])
            elif df['15_nblettres'][i] == 7 :
                words7.append(df['1_ortho'][i])
            elif df['15_nblettres'][i] == 8 :
                words8.append(df['1_ortho'][i])
            elif df['15_nblettres'][i] == 9 :
                words9.append(df['1_ortho'][i])
            else :
                words.append(df['1_ortho'][i])

    print("lenght of words1 =",len(words1))
    print("lenght of words2 =",len(words2))
    print("lenght of words3 =",len(words3))
    print("lenght of words4 =",len(words4))
    print("lenght of words5 =",len(words5))
    print("lenght of words6 =",len(words6))
    print("lenght of words7 =",len(words7))
    print("lenght of words8 =",len(words8))
    print("lenght of words9 =",len(words9))
    print("lenght of words =",len(words))


    dfwords1 = pd.DataFrame(words1)
    dfwords2 = pd.DataFrame(words2)
    dfwords3 = pd.DataFrame(words3)
    dfwords4 = pd.DataFrame(words4)
    dfwords5 = pd.DataFrame(words5)
    dfwords6 = pd.DataFrame(words6)
    dfwords7 = pd.DataFrame(words7)
    dfwords8 = pd.DataFrame(words8)
    dfwords9 = pd.DataFrame(words9)
    dfwords = pd.DataFrame(words)

    print("wrinting")

    with pd.ExcelWriter(str(letter) + " classed.xlsx") as writer: 
        if len(words1) > 0 :
            dfwords1.to_excel(writer, sheet_name=str(letter) + " words1",header=["word"],index=False)
        if len(words2) > 0 :
            dfwords2.to_excel(writer, sheet_name=str(letter) + " words2",header=["word"],index=False)
        if len(words3) > 0 :
            dfwords3.to_excel(writer, sheet_name=str(letter) + " words3",header=["word"],index=False)
        if len(words4) > 0 :
            dfwords4.to_excel(writer, sheet_name=str(letter) + " words4",header=["word"],index=False)
        if len(words5) > 0 :
            dfwords5.to_excel(writer, sheet_name=str(letter) + " words5",header=["word"],index=False)
        if len(words6) > 0 :
            dfwords6.to_excel(writer, sheet_name=str(letter) + " words6",header=["word"],index=False)
        if len(words7) > 0 :
            dfwords7.to_excel(writer, sheet_name=str(letter) + " words7",header=["word"],index=False)
        if len(words8) > 0 :
            dfwords8.to_excel(writer, sheet_name=str(letter) + " words8",header=["word"],index=False)
        if len(words9) > 0 :
            dfwords9.to_excel(writer, sheet_name=str(letter) + " words9",header=["word"],index=False)
        if len(words) > 0 :
            dfwords.to_excel(writer, sheet_name=str(letter) + " words",header=["word"],index=False)


