dias = float(input("Digite a quantidade de dias: "))
horas = float(input("Digite a quantidade de horas: h"))
minutos = float(input("Digite a quantidade de minutos: "))

total_minutos = (dias * 24 * 60) + (horas * 60) + minutos 
print(f"O total em minutos é de: {total_minutos:.2f}.")