from tkinter import *
from random import randint

def würfeln():
    global summe
    global counter
    counter +=1
    text=label.cget('text')
    zahl = randint(1,6)
    summe += zahl
    label.config(text=text + ' ' + str(zahl))
    label2.config(text=str(summe))
    label3.config(text=str(counter))
    if summe > 21:
        label.config(bg='yellow')
    if summe == 21:
        label.config(bg='green')
    
def löschen():
    global summe
    global counter
    counter=0
    summe=0
    label.config(text= ' ', bg='white')
    label2.config(text= ' ')
    label3.config(text= ' ')

summe = 0
counter = 0

#----- Widgets

fenster = Tk()
label=Label(master=fenster, width =16, font=('arial', 30), text='', bg='white')
label2=Label(master=fenster, width = 16, font=('arial', 15), text='', bg='grey')
label3=Label(master=fenster, width = 16, font=('arial', 15), text='', bg='white')
labelPlatzhalter=Label(master=fenster, width =16)
b_würfeln = Button(master=fenster, text='Würfeln', command=würfeln)
b_löschen= Button(master=fenster, text='löschen', command=löschen)

#----- layout

label.pack()
label2.pack(side=LEFT)
label3.pack(side=RIGHT)
labelPlatzhalter.pack()
b_würfeln.pack(side=LEFT, padx=30, pady=10)
b_löschen.pack(side=RIGHT, padx=30, pady=10)
fenster.mainloop()