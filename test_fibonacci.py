import unittest
from fibonacci import fibonacci

class TestFibonacci(unittest.TestCase):
    def setUp(self):
        pass
    def tearDown(self):
        pass
    def test_fibonacci_ok(self):
        lista = fibonacci(6)
        self.assertEqual(len(lista), 6, "Error en tamaño de lista")
        self.assertTrue(5 in lista and 8 in lista, "Error en calculo")
        
    def test_fibonacci_cero(self):
        lista = fibonacci(0)
        self.assertTrue(len(lista) == 0, "Error en fib(0)")

    def test_fibonacci_uno(self):
        lista = fibonacci(1)
        self.assertTrue(len(lista) == 1 and lista==[1], "Error fib(1)")
