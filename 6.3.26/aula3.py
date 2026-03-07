n1 = float(input("Escolha um número"))
n2 = float(input("Escolha um número"))
OP = input("Escolha o operação")

if OP == "+":
    print(n1+n2) 

if OP == "-":
    print(n1-n2)

if OP == "*":
    print(n1*n2)

if OP == "/" and n2!=0:
    print(n1/n2)

if OP == "%" and n2!=0:
    print(n1%n2)

if OP == "**":
    print(n1**n2)

if OP == "//" and n2!=0:
    print(n1//n2) 

