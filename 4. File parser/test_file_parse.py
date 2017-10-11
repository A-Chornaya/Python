import unittest
from file_parse import find
from file_parse import replace


class TestClassFileParse(unittest.TestCase):
    def test_input_to_find(self):
        self.assertRaises(TypeError, lambda: find(3, 'love'))
        self.assertRaises(TypeError, lambda: find('cinderella.txt', 5.6))
        self.assertRaises(TypeError, lambda: find(True, 4))

    def test_input_to_replace(self):
        self.assertRaises(TypeError, lambda: replace('file.txt',
                                                     'cinderella', 4))
        self.assertRaises(TypeError, lambda: replace('file.txt', True,
                                                     'rapuncel'))
        self.assertRaises(TypeError, lambda: replace(5.0, 'cinderella',
                                                     'rapuncel'))


if __name__ == '__main__':
    unittest.main(verbosity=2)
