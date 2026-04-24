# Lê dois valores inteiros (0 ou 1)
valor1 = int(input("Digite o primeiro valor (0 ou 1): "))
valor2 = int(input("Digite o segundo valor (0 ou 1): "))

# Converte os números 0/1 para booleanos (False/True)
bool1 = bool(valor1)
bool2 = bool(valor2)

print(f"\nResultados para {valor1} e {valor2}:")
# and: Retorna True se ambos forem True
print(f"AND: {bool1 and bool2}")

# or: Retorna True se pelo menos um for True
print(f"OR: {bool1 or bool2}")

# not: Inverte o valor do primeiro operando
print(f"NOT {valor1}: {not bool1}")
print(f"NOT {valor2}: {not bool2}")
