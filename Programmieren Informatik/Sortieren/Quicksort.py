#Quicksort

from random import *

def Partition(Liste, p):
    LListe=[]
    RListe=[]
    
    for i in Liste:
        if i < p:
            LListe.append(i)
        else:
            RListe.append(i)
    return LListe, RListe

def Quicksort(Zahlen):
    
    if len(Zahlen)>1:
        p=Zahlen[0]
        Zahlen.remove(p)
        LListe, RListe = Partition(Zahlen, p)
        
        KSortiert=Quicksort(LListe)
        GSortiert=Quicksort(RListe)
        
        LSortiert= KSortiert + [p]
        LSortiert= LSortiert + GSortiert
    else:
        LSortiert=Zahlen
        
    return LSortiert

Zahlen=[]
n=int(input("Wie viele Zahlen?"))
for i in range(0,n):
    Zahlen.append(randint(0,n*10))
    
print(Zahlen)
Zahlensortiert=Quicksort(Zahlen)
print(Zahlensortiert)