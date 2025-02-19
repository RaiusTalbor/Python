import pickle
liste=['A', 'B']
f=open('liste.dat', 'wb')
pickle.dump(liste, f)
f.close()

g=open('liste.dat', 'rb')
listenausgabe=pickle.load(g)
g.close()

print(listenausgabe)