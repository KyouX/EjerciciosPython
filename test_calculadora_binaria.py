import unittest
from unittest.mock import Mock
from calculadora_binaria import CalculadoraBinaria

class Conversor:
    pass

class TestCalculadoraBinaria(unittest.TestCase):
    def setUp(self):
        self.conversor = Conversor()
        
        def mock_btd(arg):
            diccionario_valores = {'01': 1, '10': 2}
            return diccionario_valores[arg]
        self.conversor.btd = Mock(side_effect=mock_btd)

        def mock_dtb(arg):
            diccionario_valores = {2 : '10', 0: '00'}
            return diccionario_valores[arg]
        self.conversor.dtb = Mock(side_effect=mock_dtb)
        
    def tearDown(self):
        pass
    
    def test_sumar(self):
        calculadora_binaria = CalculadoraBinaria(self.conversor)
        self.assertTrue(calculadora_binaria.sumar("01","01") == "10")

    def test_restar(self):
        calculadora_binaria = CalculadoraBinaria(self.conversor)
        self.assertTrue(calculadora_binaria.restar("01","01") == "00")



# ..
