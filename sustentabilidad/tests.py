import unittest
from .emisiones import calcular_emisiones_carbono


class TestCalculoEmisiones(unittest.TestCase):

    def test_consumo_normal(self):
        self.assertAlmostEqual(
            calcular_emisiones_carbono(100), 40.0
        )

    def test_consumo_cero(self):
        self.assertEqual(
            calcular_emisiones_carbono(0), 0
        )

    def test_consumo_decimal(self):
        self.assertAlmostEqual(
            calcular_emisiones_carbono(12.5), 5.0
        )

    def test_factor_personalizado(self):
        self.assertAlmostEqual(
            calcular_emisiones_carbono(100, 0.5), 50.0
        )

    def test_consumo_negativo(self):
        with self.assertRaises(ValueError):
            calcular_emisiones_carbono(-20)