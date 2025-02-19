from random import *
from fill import *
from time import *


#Quelle: http://www.inf-schule.de/grenzen/komplexitaet/sortieren/sortieralgorithmen/quicksort
# ALGORITHMUS quicksort
# Übergabe: Liste L
# wenn die Liste L mehr als ein Element hat:
#     # zerlegen
#     wähle als Pivotelement p das erste Element der Liste aus
#     erzeuge Teillisten K und G aus der Restliste (L ohne p) mit:
#     - alle Elemente aus K sind kleiner als das Pivotelement p
#     - alle Elemente aus G sind größergleich als das Pivotelement p
#     # Quicksort auf die verkleinerten Listen anwenden
#     KSortiert = quicksort(K)
#     GSortiert = quicksort(G)
#     # zusammensetzen
#     LSortiert = KSortiert + [p] + GSortiert
# sonst:
#     LSortiert = L
# Rückgabe: LSortiert

def partition(L, p): #L -Liste p - Pivotelement
    RList=[]
    LList=[]
    for ele in L:
        if ele<p:
            LList.append(ele)
        else:
            RList.append(ele)
    return LList, RList


def qsort(Liste):
    if len(Liste)>1:
        pivot=Liste[0]
        Liste.remove(pivot)
        Llist,RList=partition(Liste, pivot)
        #Rekursive Anwendung von Quicksort auf die linke und rechte Teilliste
        RechtsSortiert=qsort(RList)
        LinksSortiert=qsort(Llist)
        #Liste Zusammensetzen
        #LSortiert=[]
        LinksSortiert=LinksSortiert+[pivot]
        LSortiert=LinksSortiert+RechtsSortiert
    else:
        LSortiert=Liste
    return LSortiert

#Liste=fill_besser(1000, 10000)
Liste=sample(range(0,100000),100000)
print(Liste)
#Zeit messen
start=clock()
Liste=qsort(Liste)
ende=clock()
print(Liste)
print("Laufzeit", ende-start)