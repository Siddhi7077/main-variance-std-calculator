import unittest
import mean_var_std

class UnitTests(unittest.TestCase):
    def test_calculate(self):
        actual = mean_var_std.calculate([2,6,2,8,4,0,1,5,7])
        expected = {
            'mean': [[3.6666666666666665, 5.0, 3.0], [3.3333333333333335, 4.0, 4.333333333333333], 3.888888888888889],
            'variance': [[9.555555555555557, 6.0, 8.666666666666666], [8.222222222222221, 10.666666666666666, 6.333333333333333], 9.209876543209875],
            'standard deviation': [[3.0912061651652345, 2.449489742783178, 2.943920288775949], [2.8674417556808756, 3.265986323710904, 2.5166114784235836], 3.0347778408328137],
            'max': [[8, 6, 7], [8, 4, 7], 8],
            'min': [[1, 4, 0], [2, 0, 1], 0],
            'sum': [[11, 15, 9], [16, 12, 13], 35]
        }
        self.assertEqual(actual, expected, "Expected different output when calling 'calculate()' with [2,6,2,8,4,0,1,5,7]")

    def test_calculate_with_incorrect_length(self):
        with self.assertRaises(ValueError) as context:
            mean_var_std.calculate([1,2,3,4])
        self.assertEqual(str(context.exception), "List must contain nine numbers.")
