n1 = float(input("Digite o primeiro número: "))
n2 = float(input("Digite o segundo número: "))
operacao = input('Digite a operacao: ')
match operacao:
    case "+":
        resultado = n1 + n2
    case "-":
        resultado = n1 - n2
    case "/":
        if n2 == 0:
            print("Erro: divisão por zero")
            
        else:
            resultado = n1 / n2
    case "*":
        resultado = n1 * n2
    case _:
        print("Opção inválida")
        resultado = None


print(f"Resultado: {resultado:.2f}")
