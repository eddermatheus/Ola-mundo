while True:
    print("\n==== Calculadora ====")
    print("1 - Soma")
    print("2 - Subtração")
    print("3 - Multiplicação")
    print("4 - Divisão")
    print("0 - Sair")

    operacao = input("Qual operação você deseja? ").strip()

    if operacao == "0":
        print("Saindo...")
        break

    n1 = float(input("Digite o primeiro número: "))
    n2 = float(input("Digite o segundo número: "))

    match operacao:
        case "1":
            resultado = n1 + n2
        case "2":
            resultado = n1 - n2
        case "3":
            if n2 == 0:
                print("Erro: divisão por zero")
                continue
            resultado = n1 / n2
        case "4":
            resultado = n1 * n2
        case _:
            print("Opção inválida")
            continue

    print(f"Resultado: {resultado:.2f}")
