import conversions
import unittest
import conversions_refactored


class Testing(unittest.TestCase):
    ctok_values = ((500, 773.15), (60, 333.15), (40, 313.15), (-10, 263.15), (-140.00, 133.15))
    ctof_values = ((25, 77), (30, 86), (33, 91.4), (40, 104), (180, 356))
    ktof_values = ((30, -405.67), (10, -441.67), (500, 440.33), (-10, -477.67), (16, -430.87))

    p4_values = {('c', 'k'): (500, 773.15),
                 ('k', 'c'): (773.15, 500),
                 ('c', 'f'): (25, 77),
                 ('f', 'c'): (77, 25),
                 ('k', 'f'): (30, -405.67),
                 ('f', 'k'): (-405.67, 30),
                 ('m', 'y'): (10, 10.94),
                 ('y', 'm'): (10.9361, 10),
                 ('y', 'mi'): (1000, 0.568182),
                 ('mi', 'y'): (0.568182, 1000),
                 ('m', 'mi'): (1000, 0.621371),
                 ('mi', 'm'): (0.621371, 1000),
                 ('f', 'f'): (1, 1),
                 ('c', 'c'): (1, 1),
                 ('k', 'k'): (1, 1),
                 ('m', 'm'): (1, 1),
                 ('mi', 'mi'): (1, 1),
                 ('y', 'y'): (1, 1)}

    def test_c_to_k(self):
        for float1, float2 in self.ctok_values:
            result = conversions.convertCelsiusToKelvin(float1)
            self.assertAlmostEqual(float2, result, places=2, msg="Celsius to Kelvin conversion failed")

    def test_c_to_f(self):
        for float1, float2 in self.ctof_values:
            result = conversions.covertCelsiusToFahrenheit(float1)
            self.assertAlmostEqual(float2, result, places=2, msg="Celsius to Fahrenheit conversion failed")

    def test_k_to_c(self):
        for float2, float1 in self.ctok_values:
            result = conversions.convertKelvinToCelsius(float1)
            self.assertAlmostEqual(float2, result, places=2, msg="Kelvin to Celsius conversion failed")

    def test_k_to_f(self):
        for float1, float2 in self.ktof_values:
            result = conversions.convertKelvinToFahrenheit(float1)
            self.assertAlmostEqual(float2, result, places=2, msg="Kelvin to Fahrenheit conversion failed")

    def test_f_to_k(self):
        for float2, float1 in self.ktof_values:
            result = conversions.convertFahrenheitToKelvin(float1)
            self.assertAlmostEqual(float2, result, places=2, msg="Fahrenheit to Kelvin conversion failed")

    def test_f_to_c(self):
        for float2, float1 in self.ctof_values:
            result = conversions.convertFahrenheitToCelsius(float1)
            self.assertAlmostEqual(float2, result, places=2, msg="Fahrenheit to Celsius conversion failed")

    def test_convert_refactor(self):
        for units in self.p4_values:

            pre_converted = self.p4_values[units][0]
            test_value = self.p4_values[units][1]
            from_unit = units[0]
            to_unit = units[1]

            result = conversions_refactored.refactored(from_unit, to_unit, pre_converted)
            self.assertAlmostEqual(test_value, result, places=2, msg=f"From {from_unit} to {to_unit} Failed")



if __name__ == '__main__':
    unittest.main()
