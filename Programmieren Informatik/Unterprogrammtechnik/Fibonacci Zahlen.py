liste=[0]

n=int(input('n?'))

def fib(n):
    if liste[0]==1:
        liste.append(1)
        return liste
    else:
        liste[n]=liste[n-1]+liste[n-2]        
        return liste[n]

ergebnis=fib(n)

print(ergebnis)
   
#funktioniert nicht!!!!