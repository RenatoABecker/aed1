n1 = float(input("Digite a primeira nota: "))
n2 = float(input("Digite a segunda nota: "))
f = int(input("Digite o número de faltas: "))
media = (n1 + n2) / 2
if media >= 7 and f >= 5:
    print("Aprovado")
elif media >= 4 and media < 7 and f >= 5:
    print("Recuperação")    
else:    print("Reprovado")

