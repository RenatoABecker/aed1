peso = float(input("Digite o seu peso (em kg): "))
altura = float(input("Digite a sua altura (em cm): "))

#Para calcular o IMC, divide-se o peso (kg) pela altura ao quadrado (m²). Por exemplo, se você pesa 70 kg e tem 1,75 m de altura, o cálculo seria: 70 / (1,75 * 1,75) = 22,86 kg/m²

calculo = peso / (altura*2)

if calculo < 18.5:
    print("Baixo peso.")
elif 18.5 >= calculo < 25.0:
    print("Peso ideal.")
elif 25.0 >= calculo < 30.0:
    print("Sobrepeso.")
elif 30.0 >= calculo < 35.0:
    print("Obesidade grau I.")
elif 35.0 >= calculo < 40.0:
    print("Obesidade grau II.")
elif calculo >= 40.0:
    print("Obesidade grau III.")