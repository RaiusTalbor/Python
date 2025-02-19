#irgendwas im Minimum funktioniert nicht

from random import *

zufallszahlen=[]

for i in range(0,10):
    zahl=randint(0,1000)
    zufallszahlen.append(zahl)
    
print(zufallszahlen)
    
#sortieren
    
sortierliste=[]

for i in range(0, len(zufallszahlen)):
    
    #zwischenspeicher=zufallszahlen.min()
      
    a=zufallszahlen[0]
    
    for i in range(0, len(zufallszahlen)):
        if a>zufallszahlen[i]:
            a=zufallszahlen[i]

    sortierliste.append(a)
    zufallszahlen.remove(a)