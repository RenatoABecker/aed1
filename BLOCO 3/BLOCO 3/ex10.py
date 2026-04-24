ano = int(input("Digite um ano: "))

if ano > 2100:
    print("Data Inválida.")
elif ano > 1900:
    print(f"O ano que voce escolheu foi {ano}.")
elif ano < 1900:
    print("Data invalida")