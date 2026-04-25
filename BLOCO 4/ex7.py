preco = float(input("Digite o valor do produto: "))
pagamento = input("Forma de pagamento: ")

if pagamento == "á vista":
    print("Voce ganha 15% de desconto pagando á vista.") 
elif pagamento == "parcelar em 2x":
    print("Voce consegue parcelar em 2x sem juros!.")
elif pagamento == "parcelar em 3x":
    print("Voce pode parcelar em 3x com juros de 4,99.")