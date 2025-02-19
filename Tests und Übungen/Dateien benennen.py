import pickle

a=input('Wie soll die Datei heißen?')

text=['A', 'B']

PFAD=a + '.dat'

f=open(PFAD, 'wb')
pickle.dump(text, f)
f.close()

g=open(PFAD, 'rb')
listenausgabe=pickle.load(g)
g.close()

print(listenausgabe)