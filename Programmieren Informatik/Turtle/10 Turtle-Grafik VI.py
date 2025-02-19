#gestrichelte Linie zeichnen

x1=int(input("Startpunkt x?"))
y1=int(input("Startpunkt y?"))
x2=int(input("Endpunkt: x?"))
y2=int(input("Endpunkt: y?"))

import turtle

alex=turtle.Turtle()

from math import *

alex.penup()

alex.goto(x1 , y1)

alex.pendown()

m=sqrt(x2**2+y2**2)

x=m

while x>0:
    
    alex.goto(m/10)
    
    alex.penup()
    
    alex.goto(m/10)
    
    alex.pendown
    
    x=x-2*m/10