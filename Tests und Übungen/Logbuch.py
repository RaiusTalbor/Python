#Logbuch
from time import asctime

PFAD= 'log.txt'
MENÜ='''
(N)euer Eintrag
(L)ogbuch lesen
(E)nde
'''

def eintragen():
    logbuch=open(PFAD, 'a')
    eintrag=asctime()
    eintrag = eintrag + input('Neuer Eintrag: ')
    logbuch.write(eintrag+ '\n')
    logbuch.close()
    
def lesen():
    logbuch = open(PFAD, 'r')
    text = logbuch.read()
    logbuch.close()
    print(text)
    
#Hauptprogramm
    
auswahl= 0

while auswahl != 'e':
    print(MENÜ)
    auswahl=input('Auswahl: ')
    
    if auswahl=='n':
        eintragen()
    elif auswahl == 'l':
        lesen()
        
print('Auf Wiedersehen!')
