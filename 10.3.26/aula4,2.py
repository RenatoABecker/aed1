print ("Escolha um número") 
x = int(input()) 
y = x%5
z = x%3

if y == 0 and z == 0:
    print("Divisível")

else:
    print("Não divisível")