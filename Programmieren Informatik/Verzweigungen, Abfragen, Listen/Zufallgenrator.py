#komisch???

import random

n=int(input("Wie viele Elemente?"))
obergrenze=int(input("Welche Obergrenze?"))

list1=[]

for i in range(1,n+1):
    list1.append(i)
    
Liste=[]

for l in range(0,n):
    r=random.randint(0,obergrenze)-1
    Liste.append(list1[r])
    list1.remove(list1[r])
    obergrenze=obergrenze-1
    
print(Liste)
    