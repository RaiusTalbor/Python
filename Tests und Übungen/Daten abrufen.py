#Daten öffnen
eingabe=input('Welchen Text möchtest Du speichern?')
f=open('Datenbank.txt', mode='a', encoding='utf-8')
f.write(eingabe)
f.close()

g=open('Datenbank.txt', 'r', encoding='utf-8')
prüfung=g.read()
g.close
print(prüfung)