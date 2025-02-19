def fak(n):
    if n==1:
        return 1
    else:
        return n*fak(n-1)
    
l=fak(int(input("Welche Fakultät möchtest Du bilden?")))
print(l)