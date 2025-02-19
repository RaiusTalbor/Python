#Bubblesort
#Exponentielles Zeitwachstum mit der Anzahl der Elemente
import random
from time import *

def Bubblesort(liste):
    n=len(liste)
    
    for i in range(0,n-1):
        #prüfe jedes Element
        
        for index in range(0,n-i-1):
            #prüfe nur die unsortierten Elemente (i mal habe ich ja schon durchgeführt, die mussich nicht noch ma machen)
            #im ersten Durchlauf ist der letzte Wert schon sortiert (-1)
            #in jedem Durchlauf kommt ein sortiertes Element dazu (i)
            
            if liste[index] > liste[index + 1]:
                #Wenn es getauscht werden muss
                
                merk=liste[index]
                liste[index]=liste[index+1]
                liste[index+1]=merk

liste=[]
eingabe=int(input('Wie viele Zahlen?'))
    
for i in range(0,eingabe):
    zahl=random.randint(0,100)
    liste.append(zahl)

start=clock()
Bubblesort(liste)
ende=clock()
zeit=ende-start

print(liste)
print(zeit)