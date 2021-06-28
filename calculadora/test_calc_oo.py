from unittest import TestCase

import pytest
from calculadora.calculadora_oo import Adicao


class TesteCalc(TestCase):
    def test_equal_erro(self):
        self.assertNotEqual(1, 2)

    def test_equal_certo(self):
        self.assertEqual(2, 2)

    def test_adicao(self):
        adicao = Adicao()
        resultado = adicao.calcular(1, 2)
        self.assertEqual(3, resultado)

    def test_adicao_invalido(self):
        adicao = Adicao()
        with pytest.raises(TypeError):
            adicao.calcular(1, 'a')
