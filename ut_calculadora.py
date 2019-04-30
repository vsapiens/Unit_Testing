import unittest
import calculadora

class TestsSupercalculadora (unittest.TestCase):
    def setUp(self):
        self.calc = calculadora.calculadora()

    def tearDown(self):
        pass

    def test_propiedad_conmutativa(self):
        self.assertEqual(self.calc.sumar(5,7), self.calc.sumar(7,5))

    def test_restar_no_propiedad_conmutativa(self):
        self.assertNotEqual(self.calc.restar(5,3), self.calc.restar(3,5))

    def test_restar_2_y_2(self):
        calc = calculadora.calculadora()
        self.assertEqual(0,calc.restar(2,2))

    def test_sumar_2_y_2(self):
        calc = calculadora.calculadora()
        self.assertEqual(4,calc.sumar(2,2))

    def test_sumar_5_y_7(self):
        calc = calculadora.calculadora()
        self.assertEqual(12,calc.sumar(5,7))