#Turtle-Test
#Spirale in Sternform

import turtle

starspiral = turtle.Turtle()

for i in range(20):
    starspiral.fd(i*10)
    starspiral.right(144)

turtle.exitonclick()