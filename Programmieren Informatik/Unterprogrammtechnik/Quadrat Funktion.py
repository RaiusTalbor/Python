import turtle

bob=turtle.Turtle()

def quadrat(xstart, ystart, laenge):
    bob.penup()
    bob.goto(xstart, ystart)
    bob.pendown()    
    for i in range(0,4):
        bob.fd(laenge)
        bob.rt(90)
        

for l in range(0,10):
    
    quadrat(50,50,10+20*l)
    bob.rt(36)

turtle.exitonclick()