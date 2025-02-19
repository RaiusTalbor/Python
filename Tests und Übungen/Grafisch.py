from tkinter import *
from random import randint

#.pyw startet Programm direkt

def Antwort():
    stimmungg=int(stimmung.get())
    if stimmungg==0:
        label.config(text=liste[randint(0,9)])
    if stimmungg==1:
        label.config(text=liste2[randint(0,2)])

def Einsetzen():
    rückgabe=eingabe.get()
    label.config(text=rückgabe)

liste=["Hallo!", "Hi!", ":D", "^^", "Ich übernehme die Weltherrschaft!!!", ":)", "Ich hoffe, Du hattest einen schönen Tag!",
       "Seid gegrüßt!","Ich Dich auch!",":o"]
liste2=[":c", "Du sollst wieder glücklich sein.", "Sei nicht traurig. :("]

fenster=Tk()

bild= PhotoImage(file="Mono Inc..png")

label=Label(master=fenster, text=liste[randint(0,9)], font=('Courier', 20), width=40, height=5, padx=10)
großesBild=Label(master=fenster, padx=10, pady=10, image=bild)

text=Text(master=fenster, width=30, height=5, wrap=WORD, pady=5)
text.insert(END, "Hallo Du!")


Knopf=Button(master=fenster, text='Hallo zurück!', command=Antwort)
Knopf2=Button(master=fenster, text='Anderes Hallo', command=Einsetzen)

eingabe=Entry(master=fenster)

stimmung= StringVar()

fröhlich=Radiobutton(master=fenster, text="Ich bin fröhlich!", value=0, variable=stimmung)
traurig=Radiobutton(master=fenster, text="Ich bin traurig.", value=1, variable=stimmung)
fröhlich.select()

text.pack()
großesBild.pack(pady=20)
label.pack()
fröhlich.pack()
traurig.pack()
Knopf.pack(padx=10, pady=10)
eingabe.pack(padx=10, pady=10)
Knopf2.pack(padx=10,pady=10)

fenster.title('Hallo Welt!')
fenster.mainloop()