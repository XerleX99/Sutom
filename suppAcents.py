import pandas as pd
import os
import time

os.chdir(os.path.dirname(os.path.abspath(__file__)))

df = pd.read_excel("Lexique383.xlsx")
print('excel charged')
x,y = df.shape

for i in range (0,x):
    df['1_ortho'][i] = df['1_ortho'][i].replace("é","e").replace("è","e").replace("ê","e").replace("ë","e").replace("ô","o").replace("î","i").replace("ï","i")
    if i%1000 == 0:
        print(i)

    

    

    





with pd.ExcelWriter("Lexique383_bis.xlsx") as writer:
    df.to_excel(writer,index=False)