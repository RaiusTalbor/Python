n=int(input('Summe?'))

def summe(n):
    if n==1:
        return 1
    else:
        return n+summe(n-1)
    
eingabe1 = summe(n)

print(eingabe1)

for i in range(0, n):
    n=n+i
    
print(n)