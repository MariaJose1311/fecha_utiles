import unittest
from fecha_utils import dias_entre_fechas, sumar_dias, es_fin_de_semana

class TestFechaUtils(unittest.TestCase):

    def test_dias_entre_fechas(self):
        self.assertEqual(dias_entre_fechas("2024-01-01", "2024-01-31"), 30)
        self.assertEqual(dias_entre_fechas("2024-12-31", "2024-01-01"), 365)
        self.assertEqual(dias_entre_fechas("2024-02-28", "2024-03-01"), 2)  # Año bisiesto

    def test_sumar_dias(self):
        self.assertEqual(sumar_dias("2024-01-01", 10), "2024-01-11")
        self.assertEqual(sumar_dias("2024-02-28", 1), "2024-02-29")  # Año bisiesto
        self.assertEqual(sumar_dias("2024-12-31", 1), "2025-01-01")

    def test_es_fin_de_semana(self):
        self.assertTrue(es_fin_de_semana("2024-06-08"))  # Sábado
        self.assertTrue(es_fin_de_semana("2024-06-09"))  # Domingo
        self.assertFalse(es_fin_de_semana("2024-06-10")) # Lunes

if __name__ == '__main__':
    unittest.main()