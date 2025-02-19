#Quersummenberechnung nach Übungen vom 25.4.22, Nr.5

eingabe=str(input("Wie ist Deine Zahl?"))

quersumme=0
n=0

while n<len(eingabe):

    quersumme=quersumme+int(eingabe[n])
    
    n=n+1
    
print(quersumme)
    
