#Grafische Mebe Tests V4

import pickle
import random
import time
from tkinter import *

#-- Fenster initialisierung

fensterMebe1 = Tk()
fensterMebe1.title("Test 4 Mebe V1.0.0 in V2")
fensterMebe1.geometry("1000x800")

labelFensterMebe1 = Label(master=fensterMebe1,
                          width=300, height=20)

def Eingabe():
    text=entryMebe1.get()
    drucken(text)
    entryMebe1.delete(0, END)
    
def Weiter():
    global eingabetext
    eingabetext=entryMebe1.get()
    global weiterführung
    weiterführung +=1
    drucken(eingabetext)
    entryMebe1.delete(0, END)
    Programm(weiterführung)

entryMebe1=Entry(master=fensterMebe1)
knopfentry=Button(master=fensterMebe1, text="Eingabe", command=Eingabe)
knopfWeiter=Button(master=fensterMebe1, text="Weiter", command=Weiter)

#-- Packing

knopfWeiter.pack()
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
    
def Programm(sektor):
    
    global test
    global eingabetext
    
    if sektor == 1:
        drucken("Erfolgreich Programmteil 1 gestartet.")
        test = test + int(eingabetext)
        drucken("Test: "+ str(test))
        drucken('Bitte Zahl eingeben: ')
        
    if sektor == 2:
        drucken("Erfolgreich Programmteil 2 gestartet.")
        test = test + int(eingabetext)
        drucken("Test: "+ str(test))
        drucken('Bitte Zahl eingeben: ')
        
    if sektor == 3:
        drucken("Erfolgreich Programmteil 3 gestartet.")
        test = test + int(eingabetext)
        drucken("Test: "+ str(test))
        drucken('Bitte Zahl eingeben: ')
        
    if sektor >= 4:
        drucken("Erfolgreich Programmteil Ende gestartet.")
        test = test + int(eingabetext)
        drucken("Test: " + str(test))
        drucken('Bitte Zahl eingeben: ')

#neue Idee: Knopf auf get setzen, wie Standard, dann Programm dadurch in die nächste Szene springen lassen
#Dann eben jeden Teilabschnitt neu definieren und dann mit Knopf immer die Abschnitte hochzählen lassen

sektor=1
eingabetext=0
test = 5
weiterführung = 1
drucken("Gib den ersten Operanten ein und klicke dann auf Weiter.")
Programm(sektor)

#Hier Entscheidung, wo das Programm gerade ist.

#-- Mainloop

fensterMebe1.mainloop()