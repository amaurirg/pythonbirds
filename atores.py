# -*- coding: utf-8 -*-

# from __future__ import unicode_literals

import math

DESTRUIDO = 'Destruido'
ATIVO = 'Ativo'
GRAVIDADE = 10  # m/s^2


class Ator():
    """
    Classe que representa um ator. Ele representa um ponto cartesiano na tela.
    """
    _caracter_ativo = 'A'
    _caracter_destruido = ' '

    def __init__(self, x=0, y=0):
        """
        Método de inicialização da classe. Deve inicializar os parâmetros x, y, caracter e status

        :param x: Posição horizontal inicial do ator
        :param y: Posição vertical inicial do ator
        """
        self.y = y
        self.x = x
        self.status = ATIVO

    def caracter(self):
        return self._caracter_ativo if self.status == ATIVO else self._caracter_destruido

    def calcular_posicao(self, tempo):
        """
        Método que calcula a posição do ator em determinado tempo.
        Deve-se imaginar que o tempo começa em 0 e avança de 0,01 segundos

        :param tempo: o tempo do jogo
        :return: posição x, y do ator
        """
        return self.x, self.y

    def colidir(self, outro_ator, intervalo=1):
        """
        Método que executa lógica de colisão entre dois atores.
        Só deve haver colisão se os dois atores tiverem seus status ativos.
        Para colisão, é considerado um quadrado, com lado igual ao parâmetro intervalo, em volta do ponto onde se
        encontra o ator. Se os atores estiverem dentro desse mesmo quadrado, seus status devem ser alterados para
        destruido, seus caracteres para destruido também.

        :param outro_ator: Ator a ser considerado na colisão
        :param intervalo: Intervalo a ser considerado
        :return:
        """
        if self.status == DESTRUIDO or outro_ator.status == DESTRUIDO:
            return

        if abs(self.x - outro_ator.x) <= intervalo and abs(
                self.y - outro_ator.y) <= intervalo:
            self.status = DESTRUIDO
            outro_ator.status = DESTRUIDO

        # if self.status == ATIVO and outro_ator.status == ATIVO:
        #
        #     t_self = (self.x, self.y)
        #     t_outro_ator = (outro_ator.x, outro_ator.y)
        #     t1 = (self.x, self.y - intervalo)
        #     t2 = (self.x, self.y + intervalo)
        #
        #     t3 = (self.x - intervalo, self.y - intervalo)
        #     t4 = (self.x - intervalo, self.y)
        #     t5 = (self.x - intervalo, self.y + intervalo)
        #
        #     t6 = (self.x + intervalo, self.y - intervalo)
        #     t7 = (self.x + intervalo, self.y)
        #     t8 = (self.x + intervalo, self.y + intervalo)
        #
        #     if t_outro_ator in [t1, t2, t3, t4, t5, t6, t7, t8] or t_self == t_outro_ator:
        #         self.status = DESTRUIDO
        #         outro_ator.status = DESTRUIDO


class Obstaculo(Ator):
    _caracter_ativo = 'O'


class Porco(Ator):
    _caracter_ativo = '@'
    _caracter_destruido =  '+'


class DuploLancamentoExcecao(Exception):
    pass


class Passaro(Ator):
    velocidade_escalar = 10

    def __init__(self, x=0, y=0):
        """
        Método de inicialização de pássaro.

        Deve chamar a inicialização de ator. Além disso, deve armazenar a posição inicial e incializar o tempo de
        lançamento e angulo de lançamento

        :param x:
        :param y:
        """
        super().__init__(x, y)
        self._x_inicial = x
        self._y_inicial = y
        self._tempo_de_lancamento = None
        self._angulo_de_lancamento = None  # radianos

    def foi_lancado(self):
        """
        Método que retorna verdaeira se o pássaro já foi lançado e falso caso contrário

        :return: booleano
        """
        return self._tempo_de_lancamento is not None

    def colidir_com_chao(self):
        """
        Método que executa lógica de colisão com o chão. Toda vez que y for menor ou igual a 0,
        o status dos Passaro deve ser alterado para destruido, bem como o seu caracter

        """
        self.status = DESTRUIDO if self.y <= 0 else ATIVO
        # _ca= self.caracter

    def calcular_posicao(self, tempo):
        """
        Método que cálcula a posição do passaro de acordo com o tempo.

        Antes do lançamento o pássaro deve retornar o valor de sua posição inicial

        Depois do lançamento o pássaro deve calcular de acordo com sua posição inicial, velocidade escalar,
        ângulo de lancamento, gravidade (constante GRAVIDADE) e o tempo do jogo.

        Após a colisão, ou seja, ter seus status destruido, o pássaro deve apenas retornar a última posição calculada.

        :param tempo: tempo de jogo a ser calculada a posição
        :return: posição x, y
        """
        return self.x, self.y

    def lancar(self, angulo, tempo_de_lancamento):
        """
        Lógica que lança o pássaro. Deve armazenar o ângulo e o tempo de lançamento para posteriores cálculo.
        O ângulo é passado em graus e deve ser transformado em radianos

        :param angulo:
        :param tempo_de_lancamento:
        :return:
        """
        if self.foi_lancado():
            raise DuploLancamentoExcecao("Pássaro já foi lançado")
        self._angulo_de_lancamento = math.radians(angulo)
        self._tempo_de_lancamento = tempo_de_lancamento


class PassaroAmarelo(Passaro):
    _caracter_destruido = 'a'
    velocidade_escalar = 30


class PassaroVermelho(Passaro):
    _caracter_ativo = 'V'
    _caracter_destruido = 'v'
    velocidade_escalar = 20
