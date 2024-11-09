import unittest
from math_quiz import Number, Operator, Operation


class TestMathGame(unittest.TestCase):

    def test_Number(self):
        # Test if random numbers generated are within the specified range
        min_val = 1
        max_val = 10
        for _ in range(1000):  # Test a large number of random values
            random_num = Number(min_val, max_val)
            self.assertTrue(min_val <= random_num <= max_val)

    def test_Operator(self):
        # Test if the random operator is one of the expected options
        valid_operators = ['+', '-', '*']
        for _ in range(1000):  # Test a large number of random values
            operator = Operator()
            self.assertIn(operator, valid_operators, 
                          f"Operator {operator} is not in the required set of operators")

    def test_Operation(self):
        # Test various mathematical operations
        test_cases = [
            (5, 2, '+', '5 + 2', 7),     # Addition
            (3, 4, '-', '3 - 4', -1),    # Subtraction
            (9, 3, '*', '4 * 3', 27),    # Multiplication
            (7, 7, '+', '7 + 7', 14),    # Addition 
            (5, 5, '-', '5 - 5', 0),     # Subtraction 
            (8, 2, '*', '8 * 2', 16),    # Multiplication 
        ]

        for num1, num2, operator, expected_problem, expected_answer in test_cases:
            problem, answer = Operation(num1, num2, operator)
            self.assertEqual(problem, expected_problem, f"Problem mismatch: expected {expected_problem}, got {problem}")
            self.assertEqual(answer, expected_answer, f"Answer mismatch: expected {expected_answer}, got {answer}")

if __name__ == "__main__":
    unittest.main()
    