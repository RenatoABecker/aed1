numeros = []
for i in range(0, 10):
    x = int(input(f"Digite o {i+1}o número."))
    numeros.append(x)
maior = max(numeros)
menor = min(numeros)
print(f"O maior valor lido foi: {maior}")
print(f"O menor valor lido foi: {menor}")