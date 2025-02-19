#Internetdaten auslesen

from urllib.request import urlopen

try:
    print("Klara")
    url = 'http://www.textfiles.com/food/richbred.txt'
    
    #url='https://www.youtube.com'

    stream=urlopen(url)

    rohdaten=stream.read()

    stream.close()
    
    text=rohdaten.decode()
    
except:
    
    text= 'URL konnte nicht geöffnet werden!'

print(text)