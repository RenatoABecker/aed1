km = float(input("Digite o valor de quilometros percorridos: "))
t_litros = float(input("Digite o valor total de litros: "))

if t_litros > 0:
    consumo = km / t_litros
    print(f"O consumo médio do veículo é de: {consumo:.2f}.")
else: 
    print("A quantidade de litros deve ser maior que zero")