from random import *

def fill_nicht_gut(n, obergrenze):
    Liste=[]
    if obergrenze < n:
        return Liste
    else:
        count=0
        iter=0
        while count <=n:
            zufall=randint(0,obergrenze)
            iter=iter+1
            if zufall not in Liste:
                Liste.append(zufall)
                count = count +1
        print(iter)
    return Liste

def fill_besser(n, obergrenze):
    Liste=[] #Ergebnisliste
    Liste_Obergrenze=[] # Liste mit Zahlen bis Obergrenze
    for i in range(0,obergrenze+1):
        Liste_Obergrenze.append(i)
    count=1
    while count<=n:
        zufall=randint(0,obergrenze-count+1)
        Liste.append(Liste_Obergrenze[zufall])
        Liste_Obergrenze.remove(Liste_Obergrenze[zufall])
        count=count+1
    return Liste



# Testliste=fill_nicht_gut(100, 200)
# print(Testliste)
# Testliste.clear()
# Testliste=fill_besser(20,1000)
# print(Testliste)
# print(len(Testliste))
# print([Testliste])