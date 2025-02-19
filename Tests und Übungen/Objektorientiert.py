#Objektorientiertes Programmieren


#label funktioniert nicht, warum???

import tkinter

class Flasche:
    'Modell einer Flasche'
    def __init__(self, fassungsvermögen):
        self.inhalt=0
        self.max_inhalt=int(fassungsvermögen)
        self.geöffnet=False
    
    def öffnen(self):
        self.geöffnet = True
    
    def schließen(self):
        self.geöffnet = False
    
    def füllen(self, volumen):
        volumen=int(volumen)
        if self.geöffnet:
            if self.inhalt + volumen <= self.max_inhalt:
                self.inhalt += volumen                
                
    def leeren(self):
        if self.geöffnet:
            self.inhalt=0

def füllmich():
    Saxonia.öffnen()
    Saxonia.füllen(volumenn.get())
    rückmeldungen.config(text=Saxonia.inhalt)
    

fenster= tkinter.Tk()
fenster.title('Flasche')

volumenn=tkinter.Entry(master=fenster)
volumenn.insert(tkinter.INSERT,'0')
rückmeldungen=tkinter.Label(master=fenster, width=50, text='0')

Saxonia=Flasche(1000)

flasche_befüllen=tkinter.Button(master=fenster, text='Flasche füllen', command=füllmich())
flasche_leeren=tkinter.Button(master=fenster, text='Flasche leeren', command=Saxonia.leeren)


rückmeldungen.pack()
flasche_befüllen.pack()
flasche_leeren.pack()
volumenn.pack(pady=10)
fenster.mainloop()