import unittest
from fibonachi2 import fibonachi
from fibonachi2 import find_start

class TestClassFibonachi(unittest.TestCase):
    def test_valid_arg_fibonachi(self):
        # Arrange
        n = 50

        #Act
        list_fibo = fibonachi(n)
        valid_list_fibo = [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]

        # Assert
        self.assertEqual(list_fibo, valid_list_fibo)

    def test_valid_find_start(self):
        # Arrange
        k = 10
        list_fibo = [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55]
        valid_list_fibo = [13, 21, 34, 55]

        # Act
        start = find_start(k, list_fibo)
        fibo_part = list_fibo[start:len(list_fibo)]

        # Assert
        self.assertEqual(start, 7)
        self.assertEqual(fibo_part, valid_list_fibo)


if __name__ == '__main__':
    unittest.main(verbosity=2)
