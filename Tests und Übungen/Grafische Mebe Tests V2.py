import pickle
import random
import time
from tkinter import *

Anzeigenspeicher = ["A",
                    "B",
                    "C",
                    "D"]

fensterMebe1 = Tk()
fensterMebe1.title("Test Mebe V1.0.0 in V2")
fensterMebe1.geometry("1000x800")

labelFensterMebe1 = Label(master=fensterMebe1,
                          width=300, height=20)

entryMebe1=Entry(master=fensterMebe1)

def Wartenbeenden():
    EingabeEntry= entryMebe1.get()
    drucken(EingabeEntry)
    return EingabeEntry

knopfentry=Button(master=fensterMebe1, text="Eingabe", command=Wartenbeenden)

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

def eingabe(text):
    drucken(text)
    global Warte
    while Warte==0:
        pass
    Warte=0
    NeueEingabe=entryMebe1.get()

    return NeueEingabe

labelFensterMebe1.pack()
entryMebe1.pack()
knopfentry.pack()

drucken(4)
drucken(5)
drucken()

fensterMebe1.mainloop()
