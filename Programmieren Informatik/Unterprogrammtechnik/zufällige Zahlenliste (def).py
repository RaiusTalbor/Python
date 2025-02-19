from random import *

n=int(input("Wie viele Zahlen sollen in der Liste erscheinen?"))
Start=int(input("Was ist Dein Startwert?"))
Ende=int(input("Was ist Dein Endwert?"))

def FillListe(n,Start,Ende):
    liste=[]
    
    for i in range(0,n):
        liste.append( randint(Start,Ende) )
        
    return liste

print()
print(FillListe(n,Start,Ende))

Liste=FillListe(n,Start,Ende)

def Summe(ListeS):
    summe=0
    for a in ListeS:
        summe=summe+a
    return summe

print("Dies ist die Summe der Elemente:", Summe(Liste))
    