import unittest

from main import get_temperatures, get_average_temperatures, get_max_temperature


class Tests(unittest.TestCase):
    def setUp(self):
        pass

    def test_get_temperatures(self):
        expected_temperatures = {
            "2023-04-01": 21.4,
            "2023-04-02": 18.3,
            "2023-04-03": 24.95,
            "2023-04-04": 22.05,
            "2023-04-05": 20.05,
        }
        expected_max_temperature = {"max_date": "2023-04-03", "max_temperature": 25.1}
        temperatures = get_temperatures()
        self.assertEqual(expected_temperatures, temperatures[0])
        self.assertEqual(expected_max_temperature, temperatures[1])

    def test_get_average_temperatures(self):
        expected_temperatures = {
            "2023-04-01": 21.4,
            "2023-04-02": 18.3,
            "2023-04-03": 24.95,
            "2023-04-04": 22.05,
            "2023-04-05": 20.05,
        }
        temperatures = get_average_temperatures()
        self.assertEqual(expected_temperatures, temperatures)

    def test_get_max_temperatures(self):
        expected_temperature = {"max_date": "2023-04-03", "max_temperature": 25.1}
        temperature = get_max_temperature()
        self.assertEqual(expected_temperature, temperature)
