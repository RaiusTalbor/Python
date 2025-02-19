#Währungsrechner
from tkinter import *

#verbesserung: Rundung sinnvoll

D = {'Euro':1.00,
     'Zeta':2.00,
     'Gaveon':0.50,
     'Tarres':4.00,
     'Tryvaderon':1.00,
     'Pharos':0.10,
     'Velbar':100.00,
     'Servas':2.00,
     'Fewras':4.00,
     'Xobal':1.00,
     'Sjilver':1.00,
     'Zaven':1.00,
     'Arton':0.25,
     'Huvas':4.00,
     'Carrow':2.00,
     'Livasio bloudar':1.00,
     'Licaja':2.00,
     'Xanlos':2.00,
     'Zavalon':4.00}

def berechnen():
    
    geld = eingabe.get()   
    for i in ',':
        geld = geld.replace(i, '.')
        geld = float (geld)
        
    geld = geld / D[vonwährung.get()]
    ergebnis = geld * D[inwährung.get()]
    ergebnis = round(ergebnis, 5)
    
    ausgabetext = '{} {}'.format(ergebnis,inwährung.get())
    ausgabe.config(text=ausgabetext)
    
fenster= Tk()
fenster.title('Währungsrechner')

#frame1=Frame(master=fenster) vergessen ^^"
frame2=Frame(master=fenster)
frame3=Frame(master=fenster)
frame4=Frame(master=fenster)

#-----Radiobuttons

inwährung=StringVar()
vonwährung=StringVar()

#--von
veuro = Radiobutton(master=frame2, text='Euro', value='Euro', variable=vonwährung)
vzeta = Radiobutton(master=frame2, text='Zéta - BL, LY', value='Zeta', variable=vonwährung)
vgaveon = Radiobutton(master=frame2, text='Gavéon - KR, SN, Be', value='Gaveon', variable=vonwährung)
vtarres = Radiobutton(master=frame2, text='Tarres - Mo, SI', value='Tarres', variable=vonwährung)
vtryvaderon = Radiobutton(master=frame2, text='Tryvadéron - T, FL', value='Tryvaderon', variable=vonwährung)
vpharos = Radiobutton(master=frame2, text='Pharos - I', value='Pharos', variable=vonwährung)
vvelbar = Radiobutton(master=frame2, text='Velbar - Sp', value='Velbar', variable=vonwährung)
vservas = Radiobutton(master=frame2, text='Sérvas - Se', value='Servas', variable=vonwährung)
vfewras = Radiobutton(master=frame2, text='Fewras - NF', value='Fewras', variable=vonwährung)
vxobal = Radiobutton(master=frame2, text='Xobal - N, AM', value='Xobal', variable=vonwährung)
vsjilver = Radiobutton(master=frame2, text='Sjilver - SJ, ÈL', value='Sjilver', variable=vonwährung)
vzaven = Radiobutton(master=frame2, text='Zaven - BJ, SG', value='Zaven', variable=vonwährung)
varton = Radiobutton(master=frame2, text='Arton - RZ, ZN, ZV, JA', value='Arton', variable=vonwährung)
vhuvas = Radiobutton(master=frame2, text='Huvas - IL', value='Huvas', variable=vonwährung)
vcarrow = Radiobutton(master=frame2, text='Carrow - AL', value='Carrow', variable=vonwährung)
vlivasiobloudar = Radiobutton(master=frame2, text='Livasio bloudar - RzJ', value='Livasio bloudar', variable=vonwährung)
vlicaja = Radiobutton(master=frame2, text='Licaja - Zo, Va', value='Licaja', variable=vonwährung)
vxanlos = Radiobutton(master=frame2, text='Xanlos - Te, Sa', value='Xanlos', variable=vonwährung)
vzavalon = Radiobutton(master=frame2, text='Zavalon - RR', value='Zavalon', variable=vonwährung)

#--zu
ieuro = Radiobutton(master=frame3, text='Euro', value='Euro', variable=inwährung)
izeta = Radiobutton(master=frame3, text='Zéta - BL, LY', value='Zeta', variable=inwährung)
igaveon = Radiobutton(master=frame3, text='Gavéon - KR, SN, Be', value='Gaveon', variable=inwährung)
itarres = Radiobutton(master=frame3, text='Tarres - Mo, SI', value='Tarres', variable=inwährung)
itryvaderon = Radiobutton(master=frame3, text='Tryvadéron - T, FL', value='Tryvaderon', variable=inwährung)
ipharos = Radiobutton(master=frame3, text='Pharos - I', value='Pharos', variable=inwährung)
ivelbar = Radiobutton(master=frame3, text='Velbar - Sp', value='Velbar', variable=inwährung)
iservas = Radiobutton(master=frame3, text='Sérvas - Se', value='Servas', variable=inwährung)
ifewras = Radiobutton(master=frame3, text='Fewras - NF', value='Fewras', variable=inwährung)
ixobal = Radiobutton(master=frame3, text='Xobal - N, AM', value='Xobal', variable=inwährung)
isjilver = Radiobutton(master=frame3, text='Sjilver - SJ, ÈL', value='Sjilver', variable=inwährung)
izaven = Radiobutton(master=frame3, text='Zaven - BJ, SG', value='Zaven', variable=inwährung)
iarton = Radiobutton(master=frame3, text='Arton - RZ, ZN, ZV, JA', value='Arton', variable=inwährung)
ihuvas = Radiobutton(master=frame3, text='Huvas - IL', value='Huvas', variable=inwährung)
icarrow = Radiobutton(master=frame3, text='Carrow - AL', value='Carrow', variable=inwährung)
ilivasiobloudar = Radiobutton(master=frame3, text='Livasio bloudar - RzJ', value='Livasio bloudar', variable=inwährung)
ilicaja = Radiobutton(master=frame3, text='Licaja - Zo, Va', value='Licaja', variable=inwährung)
ixanlos = Radiobutton(master=frame3, text='Xanlos - Te, Sa', value='Xanlos', variable=inwährung)
izavalon = Radiobutton(master=frame3, text='Zavalon - RR', value='Zavalon', variable=inwährung)

veuro.select()
izeta.select()

#-----Labels

ausgabe = Label(master=fenster, bg='blue', fg='white', font=('Arial',25), width=15)
label=Label(master=frame4, text='Betrag: ')
labeltrennung21=Label(master=frame2,text='Zétravstar Klippenmeer', font=('Arial', 15, 'bold'))
labeltrennung22=Label(master=frame2,text='Klippische Westmeere', font=('Arial', 15, 'bold'))
labeltrennung23=Label(master=frame2,text='Klippisches Silbermeer', font=('Arial', 15, 'bold'))
labeltrennung24=Label(master=frame2,text='Klippisches Sarvadon', font=('Arial', 15, 'bold'))
labeltrennung31=Label(master=frame3,text='Zétravstar Klippenmeer', font=('Arial', 15, 'bold'))
labeltrennung32=Label(master=frame3,text='Klippische Westmeere', font=('Arial', 15, 'bold'))
labeltrennung33=Label(master=frame3,text='Klippisches Silbermeer', font=('Arial', 15, 'bold'))
labeltrennung34=Label(master=frame3,text='Klippisches Sarvadon', font=('Arial', 15, 'bold'))

eingabe=Entry(master=frame4)
button=Button(master=frame4, text='Umrechnen', command=berechnen)

ausgabe.pack(fill='x')

#----- Layout

#frame1.pack() vergessen xD
frame4.pack(side=BOTTOM)
frame2.pack(side=LEFT, fill='x', expand=True, pady=20, padx=20)
frame3.pack(side=LEFT, fill='x', expand=True, pady=20, padx=20)


#--von
veuro.pack(anchor=W)

labeltrennung21.pack(anchor=W)

vzeta.pack(anchor=W)
vgaveon.pack(anchor=W)
vtarres.pack(anchor=W)
vtryvaderon.pack(anchor=W)
vpharos.pack(anchor=W)
vservas.pack(anchor=W)
vxobal.pack(anchor=W)

labeltrennung22.pack(anchor=W)

vvelbar.pack(anchor=W)
vlivasiobloudar.pack(anchor=W)

labeltrennung23.pack(anchor=W)

vsjilver.pack(anchor=W)
vzaven.pack(anchor=W)

labeltrennung24.pack(anchor=W)

vfewras.pack(anchor=W)
varton.pack(anchor=W)
vhuvas.pack(anchor=W)
vcarrow.pack(anchor=W)
vlicaja.pack(anchor=W)
vzavalon.pack(anchor=W)


#--zu
ieuro.pack(anchor=W)

labeltrennung31.pack(anchor=W)

izeta.pack(anchor=W)
igaveon.pack(anchor=W)
itarres.pack(anchor=W)
itryvaderon.pack(anchor=W)
ipharos.pack(anchor=W)
iservas.pack(anchor=W)
ixobal.pack(anchor=W)

labeltrennung32.pack(anchor=W)

ivelbar.pack(anchor=W)
ilivasiobloudar.pack(anchor=W)

labeltrennung33.pack(anchor=W)

isjilver.pack(anchor=W)
izaven.pack(anchor=W)

labeltrennung34.pack(anchor=W)

ifewras.pack(anchor=W)
iarton.pack(anchor=W)
ihuvas.pack(anchor=W)
icarrow.pack(anchor=W)
ilicaja.pack(anchor=W)
izavalon.pack(anchor=W)

#--letztes Layout mit Schleife

label.pack(side=LEFT)
eingabe.pack(side=LEFT)
button.pack(side=LEFT)
fenster.mainloop()