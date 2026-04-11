salario = float(input("Digite o valor do salário atual: R$ "))
porcentagem = float(input("Digite o percentual de aumento desejado (%): "))

aumento = salario * (porcentagem / 100) 
novo = salario + aumento 
print(f"O valor do aumento foi de: {aumento:.2f}R$, o salário novo vai ser: {novo:.2f}R$.")