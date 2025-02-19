import pickle
import random
import time
from tkinter import *

#-- Fenster initialisierung

fensterMebe1 = Tk()
fensterMebe1.title("Test 2 Mebe V1.0.0 in V2")
fensterMebe1.geometry("1000x800")

labelFensterMebe1 = Label(master=fensterMebe1,
                          width=300, height=20)

entryMebe1=Entry(master=fensterMebe1)

def Starten():
    ergebnis = int(eingabe()) + int(eingabe())

def Wartenbeenden():
    pass

knopfentry=Button(master=fensterMebe1, text="Eingabe", command=Wartenbeenden)

knopfstart=Button(master=fensterMebe1, text="Start", command=Starten)

#-- Packing

knopfstart.pack()
labelFensterMebe1.pack()
entryMebe1.pack()
knopfentry.pack()

#-- Programm

Anzeigenspeicher = ["", "", "", ""]

def drucken(text):
    global Anzeigenspeicher
    
    AnzeigenspeicherMax=4
    Anzeigenspeicher.append(text)

    if Anzeigenspeicher[AnzeigenspeicherMax] != None:
        Anzeigenspeich=Anzeigenspeicher[0]
        Anzeigenspeicher.remove(Anzeigenspeich)

    Labeltextfinal=""
    for i in range(len(Anzeigenspeicher)):
        Zeilenumbruch="\n"
        Labeltextfinal = str(Labeltextfinal) + str(Anzeigenspeicher[i]) + str(Zeilenumbruch)

    labelFensterMebe1.config(text=Labeltextfinal)
    
def eingabe():
    leer = ""
    
    while entryMebe1.get() == leer:
        time.sleep(5)
    wert = entryMebe1.get()
    #ergibt keinen Sinn: sobald ein Wert drin, alles weg + entry wird nicht gelöscht
    
    return wert

#neue Idee: Knopf auf get setzen, wie Standard, dann Programm dadurch in die nächste Szene springen lassen
#Dann eben jeden Teilabschnitt neu definieren und dann mit Knopf immer die Abschnitte hochzählen lassen

drucken("Es erfolgt eine Berechnung. Die Summe zweier Zahlen.")

#-- Mainloop

fensterMebe1.mainloop()
