

def existiertKante(nameStartknoten, nameZielknoten):
    knotenliste=['A', 'B','C','D']
    adjazenzmatrix=[[0,1,0,0],[0,1,1,1],[1,1,0,0],[0,0,0,0]]
    
    if nameStartknoten and nameZielknoten in knotenliste:
        indexnr1=knotenliste.index(nameStartknoten)
        indexnr2=knotenliste.index(nameZielknoten)
        
        ausgabe=adjazenzmatrix[indexnr1][indexnr2]
        if ausgabe==1:
            print('Es gibt eine Kante.')
        else:
            print('Es gibt keine Kante.')
    else:
        print('Falsche Knoten!')
        
nameStartknoten=input('Startknoten?')
nameZielknoten=input('Zielknoten?')
existiertKante(nameStartknoten, nameZielknoten)