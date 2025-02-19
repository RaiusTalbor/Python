#Turtle-Quadrat

import turtle

eingabe=int(input("Welche Seitenlänge hat Dein Quadrat?"))
x=1

alex=turtle.Turtle()

while x<5:
    alex.fd(eingabe)
    alex.left(90)
    x=x+1
    
turtle.exitonclick()