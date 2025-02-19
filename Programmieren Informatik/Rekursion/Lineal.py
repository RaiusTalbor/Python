
import turtle

bob=turtle.Turtle()

def strich(mitte,hoehe):
    bob.penup()
    bob.goto(mitte,0)
    bob.pendown()
    bob.pensize(2)
    bob.goto(mitte,hoehe)

def lineal(anfang,ende,hoehe):
    mitte=(ende+anfang)//2
    if hoehe>2:
        strich(mitte,hoehe)
        hoehe=hoehe-3
        lineal(anfang,mitte,hoehe)
        lineal(mitte,ende,hoehe)

lineal(0,300,20)
turtle.exitonclick() 