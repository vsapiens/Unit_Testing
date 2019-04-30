import unittest
import ut_calculadora
import ut_expr_aritmetica

if __name__ == "__main__":
    suite = unittest.TestSuite()
    suite.addTest(unittest.makeSuite(ut_calculadora.TestsSupercalculadora))
    suite.addTest(unittest.makeSuite(ut_expr_aritmetica.TestsExprAritmetica))
    unittest.TextTestResult(verbosity=3).run(suite)
