import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'src')))
import unittest
from calculadora import calcular_desviacion_estandar, NoSePuedeCalcular

class TestDesviacionEstandar(unittest.TestCase):

    def test_lista_vacia(self):
        with self.assertRaises(NoSePuedeCalcular):
            calcular_desviacion_estandar([])

    def test_un_elemento(self):
        self.assertEqual(calcular_desviacion_estandar([5]), 0)

    def test_dos_elementos(self):
        self.assertAlmostEqual(calcular_desviacion_estandar([5, 15]), 5)

    def test_varios_elementos(self):
        self.assertAlmostEqual(calcular_desviacion_estandar([1, 2, 3, 4, 5]), 1.4142135623730951)

    def test_todos_ceros(self):
        self.assertEqual(calcular_desviacion_estandar([0, 0, 0, 0]), 0)

    def test_positivos_y_negativos(self):
        self.assertAlmostEqual(calcular_desviacion_estandar([-1, 1, -2, 2]), 1.5811388300841898)

    def test_elementos_no_numericos(self):
        with self.assertRaises(TypeError):
            calcular_desviacion_estandar([1, 'a', 3])

if __name__ == '__main__':
    unittest.main()
