soma_idades = 0
quantidade = 0

while True:
    try:
        idade = int(input("Digite uma idade (ou um número negativo para sair): "))
        
        if idade < 0:
            break
            
        soma_idades += idade
        quantidade += 1
        
    except ValueError:
        print("Por favor, digite um número inteiro válido.")

if quantidade > 0:
    media = soma_idades / quantidade
    print(f"\nTotal de idades válidas: {quantidade}")
    print(f"A média das idades é: {media:.2f}")
else:
    print("\nNenhuma idade válida foi digitada.")