def sum(n):
    if n==1:
        return 1
    else:
        return n+sum(n-1)
    
eingabe=int(input("n"))

print("Die Summe der ersten", eingabe, "Zahlen ist: ", sum(eingabe))
