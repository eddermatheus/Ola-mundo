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
        else:
            resultado = n1 / n2
    case "4":
        resultado = n1 * n2
    case _:
        print("Opção inválida")
        resultado = None

if resultado is not None:
    print(f"Resultado: {resultado:.2f}")
