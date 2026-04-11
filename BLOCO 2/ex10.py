dividendo = int(input("Digite o dividendo (número a ser dividido): "))
divisor = int(input("Digite o divisor (número pelo qual dividir): "))

if divisor == 0:
    print("Erro: Divisão por zero não é permitida.")
else:
    quociente = dividendo // divisor
    resto = dividendo % divisor
    
    print(f"Quociente inteiro: {quociente}")
    print(f"Resto da divisão: {resto}")