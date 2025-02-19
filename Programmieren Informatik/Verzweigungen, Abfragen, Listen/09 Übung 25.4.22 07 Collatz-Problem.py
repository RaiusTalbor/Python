#Collatz-Problem nach Übungen 25.4.22, Nr. 7
#unfertig

eingabe=2
#int(input("Wie lautet Deine Zahl?"))

while eingabe<1001:

    länge=0

    while eingabe!=1:    
    
        if eingabe%2==0:
            #zahl mod 2 ist gleich 0
            eingabe=eingabe/2
            #print(eingabe)
        
            länge=länge+1
        
        else:
            eingabe=3*int(eingabe)+1
            #print( eingabe )
        
            länge=länge+1
        
    if länge==10:
        print("Die Zahl mit einer Kettenlänge von 10 ist", eingabe , ".")
        
    eingabe=eingabe+1