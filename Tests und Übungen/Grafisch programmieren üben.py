#grafisch programmieren üben
#dieses Programm soll einfach nur bestimmte Sachen mit Menü anzeigen

#GPÜ V1.0.0

from random import *
from tkinter import *

#--------------Fenster<--------------------------

fenster= Tk()
fenster.title("Grafisch programmieren üben")

#--------------Labels<---------------------------

label=Label(master=fenster, text="GRAFISCH PROGRAMMIEREN ÜBEN (GPÜ) V1.0.0")
label.pack()

labelAnzeige=Label(master=fenster, text="")
labelAnzeigeErg=Label(master=fenster, text="")
    
#---------------Zahlenzeigen<--------------------    
        
def Nullbisfünf(zahlen):
        zahl=randint(0,5)
        labelAnzeigeErg.config(text=zahl)
        
def Sechsbisneun(zahlen):
        zahl=randint(6,9)
        labelAnzeigeErg.config(text=zahl)
        
def Zahlenzeigen():
    zahlen=[1,2,3,4,5,6,7,8,9,0]
    
    buttonZahlenzeigen.destroy() 
    buttonBuchstabenzeigen.destroy()
    buttonBeenden.destroy()
    
    labelAnzeige.config(text="Zahlenzeigen")
    labelAnzeigeErg.pack()
    
    buttonNullbisfünf.pack()
    buttonSechsbisneun.pack()
    buttonZurückzumHauptmenü.pack()
    
#---------------Buchstabenzeigen<----------------    

def Großbuchstaben():
    großbuchstaben=["A","B","C","D","E","F","G","H","I","J","K","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
    zahl=randint(0,len(großbuchstaben))
    Anzeige=(großbuchstaben[zahl])
    labelAnzeigeErg.config(text=Anzeige)
        
def Kleinbuchstaben():
    kleinbuchstaben=["a","b","c","d","e","f","g","h","i","j","k","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
    zahl=randint(0,len(kleinbuchstaben))
    Anzeige=(kleinbuchstaben[zahl])
    labelAnzeigeErg.config(text=Anzeige)
        
def L():
    l=["L","l"]
    zahl=randint(0,len(l))
    Anzeige=(l[zahl])
    labelAnzeigeErg.config(text=Anzeige)
    
def Buchstabenzeigen():
    buttonZahlenzeigen.destroy()
    buttonBuchstabenzeigen.destroy()
    buttonBeenden.destroy()
    
    labelAnzeige.config(text="Buchstabenzeigen")
    labelAnzeigeErg.pack()
    
    buttonGroßbuchstaben.pack()
    buttonKleinbuchstaben.pack()
    buttonL.pack()
    buttonZurückzumHauptmenü.pack()
    
    
#---------------Beenden des Programms<-----------

def Beenden():
    buttonZahlenzeigen.destroy()
    buttonBuchstabenzeigen.destroy()
    buttonBeenden.destroy()
    labelAnzeigeErg.destroy()
    
    labelAnzeige.config(text='''Programm beendet.
Auf Wiedersehen!''')

#---------------Hauptmenü <----------------------

def Hauptmenu():
    labelAnzeigeErg.destroy()
    
    buttonGroßbuchstaben.destroy()
    buttonKleinbuchstaben.destroy()
    buttonL.destroy()
    
    buttonNullbisfünf.destroy()
    buttonSechsbisneun.destroy()
    buttonZurückzumHauptmenü.destroy()
    
    labelAnzeige.pack()
    labelAnzeige.config(text="Hauptmenü")
    buttonZahlenzeigen.pack()
    buttonBuchstabenzeigen.pack()
    buttonBeenden.pack()
    
#---------------Buttons<-------------------------

#-----Hauptmenü

buttonZahlenzeigen=Button(master=fenster,
              text="Zahlen anzeigen",
              command=Zahlenzeigen())

buttonBuchstabenzeigen=Button(master=fenster,
              text="Buchstaben anzeigen",
              command=Buchstabenzeigen())

buttonBeenden=Button(master=fenster,
              text="Beenden",
              command=Beenden)

#-----Untermenü Zahlenzeigen

buttonNullbisfünf=Button(master=fenster,
              text="Zahlen von 0-5",
              command=Nullbisfünf(zahlen))

buttonSechsbisneun=Button(master=fenster,
              text="Zahlen von 6-9",
              command=Sechsbisneun(zahlen))

buttonZurückzumHauptmenü=Button(master=fenster,
              text="Zum Hauptmenü zurück",
              command=Hauptmenu())

#-----Untermenü Buchstabenzeigen

buttonGroßbuchstaben=Button(master=fenster,
              text="Großbuchstaben",
              command=Großbuchstaben())

buttonKleinbuchstaben=Button(master=fenster,
              text="Kleinbuchstaben",
              command=Kleinbuchstaben())

buttonL=Button(master=fenster,
              text="L/l",
              command=L())
    
#---------------Programm <-----------------------
    
Hauptmenu()

fenster.mainloop()

print("Testausgabe")