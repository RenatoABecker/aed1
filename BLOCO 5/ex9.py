def calculadora():
    while True:
        print("Escolha a operacao: ")
        print("1- Adicao")
        print("2- Subtracao")
        print("3- Multiplicacao")
        print("4- Divisao")
        print("5- Sair")
        escolha = input("Digite a opcao desejada: ")
        if escolha == "5":
            print("Encerrando sessao.")
            break
        x = float(input("Digite o primeiro numero: "))
        y = float(input("Digite o segundo numero: "))

        if escolha == "1":
            print(x + y)
        elif escolha == "2":
            print(x-y)
        elif escolha == "3":
            print(x*y)
        elif escolha == "4":
            if y != 0.0:
                print(x/y)
            else:
                print("opcao invalida!")
                print("---------------------------------------------------")
calculadora()