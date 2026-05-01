soma = 0

while True:
    x = int(input("Digite um número sem ser zero: "))
    if x == 0:
        break
    soma += x

print(f"A soma dos números digitados é: {soma}")