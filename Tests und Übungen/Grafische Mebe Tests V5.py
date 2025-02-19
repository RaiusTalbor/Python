#Grafische Mebe Tests V5

import pickle
import random
import time
from tkinter import *
from _thread import start_new_thread

#-- Fenster initialisierung

fensterMebe1 = Tk()
fensterMebe1.title("Test 5 Mebe V1.0.0 in V2")
fensterMebe1.geometry("1000x800")

labelFensterMebe1 = Label(master=fensterMebe1,
                          width=300, height=20)

def Eingabe():
    text=entryMebe1.get()
    drucken(text)
    entryMebe1.delete(0, END)
    #nimmt Text aus Eingabefeld, druckt den und löscht das Eingabefeld
    
def Weiter():
    global weiter
    weiter=1
    #setzt weitervariable auf weiter
    
#---------- Widgets

entryMebe1=Entry(master=fensterMebe1)
knopfentry=Button(master=fensterMebe1, text="Eingabe", command=Eingabe)
knopfWeiter=Button(master=fensterMebe1, text="Weiter", command=Weiter)

#-- Packing

knopfWeiter.pack()
labelFensterMebe1.pack()
entryMebe1.pack()
knopfentry.pack()

#-- Druckfunktion

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
    
    #Hat einen Anzeigenspeicher, der die letzten vier Zeilen speichert
    #bei neuer Eingabe, hinten dran gehangen
    #wenn überschreitet, wird das erste Element gelöscht
    #druckt alle Zeilen ins Label, in dem jedes neue Zeile
    
#-- Funktionen für Programm

def randzahl():
    zahl = eingabe('Operant 3:')
    zahl = int(zahl)
    
    return zahl

def rechnen(operant1, operant2):
    ergebnis = operant1 + operant2
    ergebnis = ergebnis + randzahl()
    return ergebnis
    
def eingabe(text):
    global weiter
    drucken(text)
    
    while weiter == 0:
        pass
    
    weiter=0
    
    global eingabetext
    eingabetext=entryMebe1.get()
    drucken(eingabetext)
    entryMebe1.delete(0, END)
    return eingabetext

    #gibt Text aus
    #wartet, bis eine Eingabe gemacht wurde: Nutzer muss zur Weiterführung Knopf drücken
    #setzt dann weiterführung wieder zurück
    #nimmt Text aus Entry wieder raus, druckt und setzt Label wieder raus
    #gibt Text zurück, damit Programm witer rechnen kann

def Programm():
    
    global test
    global eingabetext
    
    operant1 = eingabe('Op1: ')
    
    operant2 = eingabe('Op2:')
    operant1=int(operant1)
    operant2=int(operant2)
    
    ergebnis=rechnen(operant1, operant2)
    drucken(ergebnis)
    
    #Programm läuft, immer wenn er somachen ausführt, wird Wert zurück gegeben
    #geht danach völlig unbeirrt weiter

weiter=0
eingabetext=0
drucken("Gib den ersten Operanten ein und klicke dann auf Weiter.")

start_new_thread(Programm, ())
#Damit wird das imperative Programm gestartet, New Thread ist wichtig, damit in While-Schleife nicht aufhängt.
#Problem: imperatives Programm und GUI laufen parallel

#-- Mainloop

fensterMebe1.mainloop()