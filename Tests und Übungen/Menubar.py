#So funktioniert die Menubar

from tkinter import *

fenster = Tk()
fenster.title("Menubar")
fenster.geometry("400x400")

label=Label(master=fenster, text="MENUBAR V1.0.0")
label.pack()

#Menü erstellen
my_menu = Menu(fenster) #für jedes Fenster extra Menü z.B., Fkt. zuweisen
fenster.config(menu=my_menu) #hinzufügen

# Befehle
def a():
    label.config(text="Hallo Welt!!")
    #print("Hallo Welt!")
    #pass
    
def b():
    label.config(text="Hallo Weltttt!!")

#Create menu item

erstesmenu=Menu(my_menu) #Zuweisung, wohin es gehört
my_menu.add_cascade(label="erstes", menu=erstesmenu) #Menü hinzugefügt
erstesmenu.add_command(label="Hi!", command=a) #Item hinzugefügt
erstesmenu.add_command(label="Hi!!", command=a)
erstesmenu.add_separator() #Trennstrich
erstesmenu.add_command(label="Hi!!!", command=a)

##

zweitesmenu=Menu(my_menu) #Zuweisung, wohin es gehört
my_menu.add_cascade(label="zweites", menu=zweitesmenu) #Menü hinzugefügt
zweitesmenu.add_command(label="Hallo", command=b) #Item hinzugefügt
zweitesmenu.add_command(label="Hallo!!", command=b)
zweitesmenu.add_separator() #Trennstrich
zweitesmenu.add_separator()
zweitesmenu.add_command(label="Hallo!!!", command=b)

fenster.mainloop()