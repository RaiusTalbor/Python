import turtle
import random
import math

eingabe=int(input("Wie oft soll die Simulation durchgeführt werden?"))
entfernung=[]
ergebnis=0

turtle.tracer(0,0)

alex=turtle.Turtle()

alex.left(90)

for l in range(0,eingabe):
    
    for i in range(0,1000):
        #1000 Schritte
        z=random.randint(0,3)
        #zufällige Richtung wird ausgewählt
        
        if z==0:
            alex.right(0)
        elif z==1:
            alex.right(90)
        elif z==2:
            alex.right(180)
        else:
            alex.left(90)
            
        alex.fd(1)
        #er geht die Richtung

    entfernung.append(math.sqrt((alex.xcor()**2)+(alex.ycor()**2))) 
    #print("Er ist", entfernung, "Schritte entfernt.")
    ergebnis=ergebnis+entfernung[l]
    
ergebnis=ergebnis/len(entfernung)
print(ergebnis)
#durchschnittliches Ergebnis        

turtle.update()
turtle.exitonclick()