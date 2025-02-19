TEL= [('Mathias', '999'),
      ('Bea', '888'),
      ('Marius', '333')]

MENÜ= '''
(T)elefonnummer suchen
(N)ame suchen
(E)nde
'''

def suche_nummern(suchwort):
    for name, nummer in TEL:
        if suchwort in name:
            print(' ')
            print(name, nummer)
        #else:
            #print('Nicht gefunden')
            
def suche_namen(ziffern):
    for name, nummer in TEL:
        if ziffern in nummer:
            print(' ')
            print(name, nummer)
        #else:
            #print('Nicht gefunden')
        
print(MENÜ)
eingabe=input('Auswahl (t, n, e): ')

while eingabe != 'e':
    if eingabe == 't':
        suchwort = input('Suchwort: ')
        
        suche_nummern(suchwort)
        
    elif eingabe == 'n':
        ziffern = input('Ziffern: ')
        
        suche_namen(ziffern)
        
    else:
        print('''
Falsche Eingabe!''')
        
    print(MENÜ)
    eingabe=input('Auswahl (t, n, e): ')
    
print('''
Bis bald! :D
''')