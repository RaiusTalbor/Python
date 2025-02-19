passwort="Hallo"

passworteingabe=1

Fehlversuche=1

passworteingabe=input("Passwort?")

while passworteingabe!=passwort:
    if Fehlversuche != 3:
        Fehlversuche=Fehlversuche+1
        input("Passwort?")
    else:
        print("Keine weiteren Versuche!")
        passworteingabe="Hallo"
        
print("Passwort ist richtig!")