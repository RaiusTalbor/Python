from turtle import *

def quadrat(startx,starty,laenge):
    penup()
    goto(startx, starty)
    pendown()
    for _ in range(0,4):
        fd(laenge)
        rt(90)

def quadrat_1(startx, starty, laenge):
    for i in range(0,9):
        quadrat(startx+ i*20,starty, laenge)

def quadrat_2(startx, starty, laenge):
    if startx<=230:
        quadrat(startx, starty, laenge)
        startx=startx+20
        quadrat_2(startx, starty,laenge)

quadrat_1(50,50,100)
quadrat_2(50,200,100)


