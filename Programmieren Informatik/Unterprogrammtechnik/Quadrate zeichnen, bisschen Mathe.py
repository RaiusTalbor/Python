#Quadrat zeichnen, dann ein weiteres, dessen Diagonale so groß ist, wie Seitenlänge vorher

import math
import turtle

x=int(input("Wie lang ist die Seitenlänge?"))

turtle.tracer(0,0)

alex=turtle.Turtle()

alex.penup()    
alex.bk(x*2)
alex.pendown()

def quadrat(x):    
    for i in range(0,4):
        alex.fd(x)
        
        alex.left(90)

while x>=1:

    quadrat(x)
    
    alex.fd(x)
    
    x=math.sqrt(x**2/2)
    
turtle.update()
    
turtle.exitonclick()