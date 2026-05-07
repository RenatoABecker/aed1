x = int(input("Digite um número inteiro: "))

if x <= 1:
    print(f"{x} não é primo.")
else:
    eh_primo = True
    for i in range (2, x): 
        if x % i == 0:
            eh_primo = False
            break
    if eh_primo:
        print(f"{x} é primo.")
    else:
        print(f"{x} não é primo.")