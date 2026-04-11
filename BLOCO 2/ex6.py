p = float(input("Digite o valor do produto: "))
per = float(input("Digite o percentual de desconto: "))

desconto = (p*per) / 100
pagar = p - desconto
print(f"O valor que deverá ser pago ao produto é de: {pagar:.2f}R$.")