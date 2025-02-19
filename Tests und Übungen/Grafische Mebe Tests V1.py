# from tkinter import *
# 
# fensterMebe1 = Tk()
# fensterMebe1.title("Mebe V1.0.0")
# fensterMebe1.geometry("1000x800")
# 
# labelFensterMebe1 = Label(master=fensterMebe1, width=25, height=10)
# 
# labelFensterMebe1.pack()
# 
# labelFensterMebe1.config(text="Hallo")
# 
# fensterMebe1.mainloop()

Anzeigenspeicher=[1,2,3,4,5]

def drucken(text):
    
    global Anzeigenspeicher
    
    Anzeigenspeicher.append(text)
    leer = None

    if Anzeigenspeicher[5] != leer:
        Anzeigenspeich=Anzeigenspeicher[0]
        Anzeigenspeicher.remove(Anzeigenspeich)
        
    return Anzeigenspeicher
        
print(drucken(6))

eingabe=input("Tralala")

print(drucken(eingabe))