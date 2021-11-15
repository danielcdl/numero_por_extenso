import sys
import unittest
sys.path.insert(0, './numero_por_extenso')

import numero_por_extenso

from testes import formatar_numero_testes, real_testes, monetario_testes


class TestNumeroPorExtenso(unittest.TestCase):

    def test_formatar_numero(self):
        for saida, numeros in formatar_numero_testes:
            for entrada in numeros:
                self.assertEqual(numero_por_extenso.formatar_numero(entrada), saida)

    def test_real(self):
        for teste in real_testes:
            for numero in teste[1:]:
                self.assertEqual(numero_por_extenso.real(numero), teste[0])

    def test_monetario(self):
        for teste in monetario_testes:
            for numero in teste[1:]:
                self.assertEqual(numero_por_extenso.real(numero), teste[0])

if __name__ == '__main__':
    unittest.main()