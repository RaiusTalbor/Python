#Schleifen

for i in range(1, 101):
    print(i)
    
print("")
    
#i nimmt alle Werte nacheinander an; ANNEHMEN!
#für die Länge von i automatisch jedes Element durchgehen mit folgendem Befehl: print
#ich kann einen dritten Parameter einfügen, dann ist es der Abstand
    
for t in range(1, int(input("Obergrenze?"))+1):
    print(t)
    
print("")
    
zeichenkette=input("Deine Zeichenkette?")
i=0
for n in zeichenkette:
    i=i+1
    print("Der", str(i) + ". Buchstabe ist:", str(n))