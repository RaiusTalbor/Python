#Fahrt nach Dresden Rechner
#Fadre V1.0.0

spritpreis = float(input("Spritpreis: "))
verbrauch = float(input("Verbrauch pro 100 km: "))
#graf für mehrere Verbräuche?

verbrauchkonst = 2*spritpreis * verbrauch / 100
#+Rückweg

#Ticketpreise
tag1 = 7.20
tag2 = 9.90
vtag = 16.10

woche1 = 20.90
woche2 = 31.10
uwoche = 46.60     #umliegende zonen
vwoche = 61.40

dticket = 58

jobticket = 25.55

tage = float(input("Anzahl der Tage: "))
wochen = float(round(tage/7))
if wochen == 0:
    wochen=1
monate = float(round(wochen/4))
if monate == 0:
    monate=1

#Spritgeld zur Station
coswigkonst = 4*verbrauchkonst*tage*2
zitzschewigkonst = 3*verbrauchkonst*tage*2
kaditzkonst = 8.5*verbrauchkonst*tage*2
trachaukonst = 4.2*verbrauchkonst*tage*2
uferkonst = 18*verbrauchkonst*tage*2
freibergerkonst = 20.1*verbrauchkonst*tage*2

print("")
print("")

print("Fahrt ohne Öffis: ", 15.2*verbrauchkonst*tage)

if tage*tag1 < woche1:
    print("")
    print("")

    print("Tagesticket Dresden Einstieg Trachau: ", trachaukonst+tage*tag1)
    print("Tagesticket Dresden Einstieg Kaditz: ", kaditzkonst+tage*tag1)
    print("Tagesticket Dresden Einstieg Uferstr.: ", uferkonst+tage*tag1)
    print("Tagesticket Dresden Einstieg Freiberger Str.: ", freibergerkonst+tage*tag1)
    
if tage*tag2 < woche2:
    print("Tagesticket (2Z) Dresden Einstieg Zitzschewig: ", zitzschewigkonst+tage*tag2)
    
if tage*vtag < vwoche:
    print("Tagesticket (V) Dresden Einstieg Coswig: ", coswigkonst+tage*vtag)

print("")
print("")
   
print("Wochenticket (1Z) Dresden Einstieg Trachau: ", trachaukonst+wochen*woche1)
print("Wochenticket (1Z) Dresden Einstieg Kaditz: ", kaditzkonst+wochen*woche1)
print("Wochenticket (1Z) Dresden Einstieg Uferstr.: ", uferkonst+wochen*woche1)
print("Wochenticket (1Z) Dresden Einstieg Freiberger Str.: ", freibergerkonst+wochen*woche1)
print("Wochenticket (2Z) Dresden Einstieg Zitzschewig: ", zitzschewigkonst+wochen*woche2)
print("Wochenticket (umliegend) Dresden Einstieg Coswig: ", coswigkonst+wochen*uwoche)
print("Wochenticket (V) Dresden Einstieg Coswig: ", coswigkonst+wochen*vwoche)

print("")
print("")

print("Deutschlandticket Dresden Einstieg Coswig: ", coswigkonst+monate*dticket)
print("Job-D-Ticket Dresden Einstieg Coswig: ", coswigkonst+monate*jobticket)

print("")
print("")