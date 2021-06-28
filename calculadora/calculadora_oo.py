class Operacao():
    def calcular(self, operando1, operando2):
        not NotImplementedError()


class Calculadora():
    """ Obter inputs de usuários e conter operações """
    def __init__(self):
        self.operacoes = {}

    def adicionar_operacao(self, sinal, operacao):
        self.operacoes[sinal] = operacao

    def executar(self):
        operando1 = float(input("Digite o primeiro operando: "))
        operando2 = float(input("Digite o segundo operando: "))
        sinal = input("Digite o sinal da operação: ")
        operacao_escolhida = self.operacoes[sinal]
        return operacao_escolhida.calcular(operando1, operando2)


class Adicao(Operacao):
    def calcular(self, operando1, operando2):
        return operando1 + operando2


class Resto(Operacao):
    def calcular(self, operando1, operando2):
        return operando1 % operando2


adicao = Adicao()
resto = Resto()
calculadora = Calculadora()
calculadora.adicionar_operacao("+", adicao)
calculadora.adicionar_operacao("%", resto)
