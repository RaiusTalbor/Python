#Turtle - Test

import turtle

painter=turtle.Turtle()

painter.pencolor("blue")

for i in range(50):
    painter.fd(50)
    painter.left(123)
painter.pencolor("red")

painter.penup()

painter.goto(50,50)

painter.pendown()

for i in range(50):
    painter.fd(100)
    painter.left(123)
    
turtle.exitonclick()