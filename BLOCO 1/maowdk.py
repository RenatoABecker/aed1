def daneilviadao(n):
    if n == 0:
        return 1
    else:
        return(n*daneilviadao(n-1))
    
n = 5
print(daneilviadao(n))