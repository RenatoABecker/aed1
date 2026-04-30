idade = int(input("Digite a idade: "))

if idade <= 14:
    print("Você é uma criança.")
elif idade <= 18:
    print("Você é um adolescente.")
elif idade < 60:
    print("Você é um adulto.")
else:
    print("Você é um idoso.")