import turtle
bob=turtle.Turtle()

def koch(n, grosse):
    if n==0:
        bob.fd(groesse)
    else:
        koch(n-1, groesse)
        bob.lt(60)
        koch(n-1, groesse)
        bob.rt(120)
        koch(n-1, groesse)
        bob.lt(60)
        koch(n-1, groesse)
        
n=int(input("Stufe?"))
groesse=5
koch(n, groesse)
turtle.exitonclick()