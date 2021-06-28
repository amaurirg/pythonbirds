def calcular():
    operando1 = float(input("Digite o primeiro operando: "))
    operando2 = float(input("Digite o segundo operando: "))
    sinal = input("Digite o sinal da operação: ")

    if sinal == "+":
        return operando1 + operando2
    elif sinal == "-":
        return operando1 - operando2
    else:
        return "Operação não permitida!"
