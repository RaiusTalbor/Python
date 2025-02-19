Aufgabe=input("Welche Aufgabe soll bearbeitet werden?")

if Aufgabe==str(1):
    print("Reihenfolge von Zahlen prüfen")
    
    a=input("Definiere a")
    b=input("Definiere b")
    c=input("Definiere c")
    
    if a>=b:
        print("Falsch")
    elif b>=c:
        print("Falsch")
    else:
        print("Richtig")

elif Aufgabe==str(2):
    Einzelpreis=1.8
    Anzahl=input("Wie viel Stück?")
    
    if Anzahl<10:
    elif Anzahl<50:
        