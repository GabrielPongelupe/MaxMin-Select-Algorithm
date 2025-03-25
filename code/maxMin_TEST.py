import unittest
from maxMinAlgorithm import find_min_max  # Importando a função do outro arquivo

class TestFindMinMax(unittest.TestCase):
    def test_lista_pequena(self):
        arr = [42, 17, 8]
        self.assertEqual(find_min_max(arr, 0, len(arr) - 1), (8, 42))

    def test_numeros_decrescentes(self):
        arr = [50, 40, 30, 20, 10]
        self.assertEqual(find_min_max(arr, 0, len(arr) - 1), (10, 50))

    def test_elemento_unico(self):
        arr = [-99]
        self.assertEqual(find_min_max(arr, 0, len(arr) - 1), (-99, -99))

    def test_numeros_misturados(self):
        arr = [15, -3, 22, 0, 7, -8]
        self.assertEqual(find_min_max(arr, 0, len(arr) - 1), (-8, 22))

    def test_valores_grandes(self):
        arr = [100000, 500000, 999999, 250000, 750000]
        self.assertEqual(find_min_max(arr, 0, len(arr) - 1), (100000, 999999))

    def test_lista_com_numeros_negativos(self):
        arr = [-5, -10, -3, -1, -7]
        self.assertEqual(find_min_max(arr, 0, len(arr) - 1), (-10, -1))

    def test_lista_ordenada_crescente(self):
        arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        self.assertEqual(find_min_max(arr, 0, len(arr) - 1), (1, 10))

    def test_lista_ordenada_decrescente(self):
        arr = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
        self.assertEqual(find_min_max(arr, 0, len(arr) - 1), (1, 10))

    def test_lista_com_valores_repetidos(self):
        arr = [5, 5, 5, 5, 5]
        self.assertEqual(find_min_max(arr, 0, len(arr) - 1), (5, 5))

if __name__ == "__main__":
    unittest.main()
