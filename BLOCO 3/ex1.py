x = float(input("Digite um número: "))
y = float(input("Digite um número: "))

if x > y:
    print(f"{x} é maior do que {y}.")
elif x == y:
    print("Os números escolhidos sao iguais.")
elif x < y:
    print(f"{x} é menor do que {y}.")
else:
    print(f"{x} é diferente de {y}.")