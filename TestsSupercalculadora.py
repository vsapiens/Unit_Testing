import unittest
import supercalculadora


class TestsSupercalculadora (unittest.TestCase):
    def setUp(self):
        self.calc = supercalculadora.Supercalculadora()

    def tearDown(self):
        pass

    def test_propiedad_conmutativa(self):
        self.assertEqual(self.calc.sumar(5,7), self.calc.sumar(7,5))

    def test_sumar_2_y_2(self):
        calc = supercalculadora.Supercalculadora()
        self.assertEqual(4,calc.sumar(2,2))

    def test_sumar_5_y_7(self):
        calc = supercalculadora.Supercalculadora()
        self.assertEqual(12,calc.sumar(5,7))


if __name__ == "__main__":
    unittest.main()