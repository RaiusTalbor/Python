import turtle
bob=turtle.Turtle()
bob.goto(0,0)
bob.setheading(270)


def binBaum(l):
    if l>20:
        bob.fd(l)
        bob.lt(90)
        bob.fd(l//2)
        #Position merken
        #Grund: bob ist "global" - beim Abstieg werden Attribute geändert
        x=bob.xcor()
        y=bob.ycor()
        richtung=bob.heading()
        bob.rt(90)
        binBaum(l//2)
        #Position wieder setzen beim Aufstieg
        bob.penup()
        bob.goto(x,y)
        bob.setheading(richtung)
        bob.pendown()
        bob.rt(180)
        bob.fd(l)
        bob.lt(90)
        binBaum(l//2)

binBaum(200)
turtle.exitonclick()