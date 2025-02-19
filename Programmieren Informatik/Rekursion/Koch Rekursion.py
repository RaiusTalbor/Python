import turtle
import random

n=int(input('Wie viele Stufen?'))

turtle.Turtle()

def farbe():
    zahl=0
#     zahl=random.randint(1,5)
#     farben=[green, red, yellow, blue, black]
#     pen.color()=farben[zahl]

def koch(n):
    if n==0:
        turtle.fd(5)
    else:
        farbe()
        koch(n-1)
        turtle.left(60)
        farbe()
        koch(n-1)
        turtle.right(120)
        farbe()
        koch(n-1)
        turtle.left(60)
        farbe()
        koch(n-1)
        
koch(n)

turtle.exitonclick()
        