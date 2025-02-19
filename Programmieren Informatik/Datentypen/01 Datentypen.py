#Test

#System deklariert Datentyp selbst

#wenn ich etwas aus der Mathebibliothek nehmen möchte, dann:
from math import *

x=3
y=4.5
z=x
z=x+y

eingabe0=input("Deine Zahl?")          #oder str(inout(...))
eingabe1=int(input("Deine Zahl?"))
eingabe2=float(input("Deine Zahl?"))

print(23)
print("Hallo")

eingabe3=input("Dein Name?")
print("Hallo", eingabe3)               #verbindet Zeichenketten mit Leerzeichen, + macht das auch, aber: Variabel str() davor! sonst Fehler, weil er float und str addieren will!