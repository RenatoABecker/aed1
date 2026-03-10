print("Quantas horas?") 
x = int(input()) 
y = 10+(x-1+5*x)
z = 20+(x-1+8*x)

if x<1:
    print("Grátis") 

if x>=1 and x<=3:
    print(y)

if x>3:
    print(z)