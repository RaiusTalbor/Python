def insertionSort(liste):
    
    for i in range(1, len(liste)):
        
        aktuellesElement = liste[i]
        letzterWert=i-1
        
        while letzterWert >= 0 and aktuellesElement < liste[letzterWert]:
            
            liste[letzterWert + 1] = liste[letzterWert]
            letzterWert = letzterWert - 1
            
        liste[letzterWert + 1] = aktuellesElement
        
Zufallsliste = [9, 5, 1, 4, 3]
insertionSort(Zufallsliste)
print('Sortierte Liste:')
print(Zufallsliste)