import unittest
from sequence2 import numb_seq
from sequence2 import NotPositiveNumberError


class TestClassSequence(unittest.TestCase):
    def test_valid_number_for_seq(self):
        # Arrange
        n = 100
        valid_seq = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

        # Act
        seq = numb_seq(n)

        # Assert
        self.assertEqual(seq, valid_seq)

    def test_arg_not_a_number(self):
        # Act and Arrange
        self.assertRaises(ValueError, numb_seq, '100')
        self.assertRaises(ValueError, numb_seq, 55.0)
        self.assertRaises(ValueError, numb_seq, True)

    def test_arg_not_positive_number(self):
        # Act and Arrange
        self.assertRaises(NotPositiveNumberError, numb_seq, -4)


if __name__ == '__main__':
    unittest.main(verbosity=2)
