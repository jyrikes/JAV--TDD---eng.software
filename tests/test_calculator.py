import unittest
from calculator import Calculator

class Test_calculator(unittest.TestCase):
    
    def test_soma_com_dois_numeros_positivos(self):
        c = Calculator()
        self.assertEqual(c.soma(2, 8), 10)
        
    def test_soma_com_um_numero_negativo(self):
        c = Calculator()
        self.assertEqual(c.soma(-3, 7), 4)

    def teste_soma_com_dois_numeros_negativos(self):
        c = Calculator()
        self.assertEqual(c.soma(-3, -4), -7)

    def teste_soma_com_um_zero(self):
        c =  Calculator()
        self.assertEqual(c.soma(0, 10), 10)
    
    def test_soma_com_apenas_um_numero(self):
        c = Calculator()
        self.assertEqual(c.soma(None, 10), None)
    
    def teste_soma_com_numeros_decimais(self):
        c = Calculator()
        self.assertEqual(c.soma(3.4, 7.3), 10.7)

    def teste_soma_com_valores_nao_sendo_numero(self):
        c = Calculator()
        self.assertEqual(c.soma("abc", 7), None)

    def teste_subtracao_com_dois_numeros_positivos(self):
        c = Calculator()
        self.assertEqual(c.subtracao(2, 8), -6)

    def teste_subtracao_com_um_numero_negativo(self):
        c = Calculator()
        self.assertEqual(c.subtracao(-3, 7), -10)

    def teste_subtracao_com_dois_numeros_negativos(self):
        c = Calculator()
        self.assertEqual(c.subtracao(-3, -4), 1)

    def teste_subtracao_com_um_zero(self):
        c = Calculator()
        self.assertEqual(c.subtracao(0, 10), -10)

    def test_subtracao_com_apenas_um_numero(self):
        c = Calculator()
        self.assertEqual(c.subtracao(None, 10), None)
    
    def teste_subtracao_com_numeros_decimais(self):
        c = Calculator()
        self.assertEqual(c.subtracao(3.4, 7.3), -3.9)

    def teste_subtracao_com_valores_nao_sendo_numero(self):
        c = Calculator()
        self.assertEqual(c.subtracao("abc", 7), None)

    def test_multiplicacao_com_dois_positivos(self):
        c = Calculator()
        self.assertEqual(c.multiplicacao(2, 8), 16)

    def test_multiplicacao_com_um_negativo(self):
        c = Calculator()
        self.assertEqual(c.multiplicacao(-3, 7), -21)

    def test_multiplicacao_com_dois_negativos(self):
        c = Calculator()
        self.assertEqual(c.multiplicacao(-3, -4), 12)

    def test_multiplicacao_com_zero(self):
        c = Calculator()
        self.assertEqual(c.multiplicacao(0, 10), 0)

    def test_multiplicacao_com_apenas_um_numero(self):
        c = Calculator()
        self.assertEqual(c.multiplicacao(None, 10), None)

    def test_multiplicacao_com_decimais(self):
        c = Calculator()
        self.assertEqual(c.multiplicacao(3.4, 7.3), 24.82)

    def test_multiplicacao_com_valores_nao_sendo_numero(self):
        c = Calculator()
        self.assertEqual(c.multiplicacao("ABC", 7), None)

    def test_divisao_com_dois_positivos(self):
        c = Calculator()
        self.assertEqual(c.divisao(2, 8), 0.25)

    def test_divisao_com_um_negativo(self):
        c = Calculator()
        self.assertEqual(c.divisao(6, -3), -2)

    def test_divisao_com_dois_negativos(self):
        c = Calculator()
        self.assertEqual(c.divisao(-3, -4), 0.75)

    def test_divisao_com_zero(self):
        c = Calculator()
        self.assertEqual(c.divisao(0, 10), 0)
    
    def test_divisao_com_zero_no_divisor(self):
        c = Calculator()
        self.assertEqual(c.divisao(10, 0), None)

    def test_divisao_com_apenas_um_numero(self):
        c = Calculator()
        self.assertEqual(c.divisao(None, 10), None)

    def test_divisao_com_decimais(self):
        c = Calculator()
        self.assertEqual(c.divisao(7.5, 2.5), 3)

    def test_divisao_com_valores_nao_sendo_numero(self):
        c = Calculator()
        self.assertEqual(c.divisao("ABC", 7), None)
   

if __name__ == '__main__':
    unittest.main()