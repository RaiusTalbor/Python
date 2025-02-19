liste = ["spam", 23 , "L" , 12346789]

Ausgabe=liste[0]

print(Ausgabe, ", Gibt Nulltes Element an.")

Ausgabe2= liste[2]

print(Ausgabe2, ", Gibt zweites Element an.")

Ausgabe3=liste[-2]

print(Ausgabe3, ", Gibt zweites Element von hinten an.")

Ausgabe4=liste[1:-1]

print(Ausgabe4, ", Gibt erstes bis zum vorletzten Element an.")

Ausgabe5=liste[:2] + ['Th', 2*2]

print(Ausgabe5, ", Gibt alle Elemente bis zum zweiten Element an. Gibt zusätzlich ein Wort und eine errechnete Zahl aus")

Ausgabe6=3*liste[:3] + ['Buh!']

print(Ausgabe6 + [", Gibt drei Mal den Befehl hinter der Liste aus."])

#mit eckigen Klammern kann das + wieder verwendet werden.

#Methoden

len(liste) #Länge Liste

list.append(5) #fügt am Ende ein neues Element hinzu

list.extend([6, 7, 8]) #Liste wird um diese Elemente erweitert, können auch weitere Listen sein

list.insert(10, LLL) #fügt an Stelle 10 LLL ein, keine Leerstellen! out of range

list.remove(90) #entfernt erste 90 aus Liste

list.index(d) #gibt Index an, wo als erstes d vorkommt

list.count(2) #zählt, wie oft 2

