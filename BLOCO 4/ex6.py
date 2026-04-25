lado1 = float(input("Digite o lado 1: "))
lado2 = float(input("Digite o lado 2: "))
lado3 = float(input("Digite o lado 3: "))

if (lado1 + lado2 > lado3) and (lado1 + lado3 > lado2) and (lado2 + lado3 > lado1):
    print("Os lados formam um triângulo: ", end="")
    
    if lado1 == lado2 == lado3:
        print("Equilátero")
    elif lado1 != lado2 and lado1 != lado3 and lado2 != lado3:
        print("Escaleno")
    else:
        print("Isósceles")
else:
    print("Os lados informados não formam um triângulo.")
