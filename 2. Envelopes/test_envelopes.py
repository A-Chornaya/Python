import unittest
from Envelopes2 import *

class TestClassEnvelope(unittest.TestCase):
    def test_valid_envelope(self):
        self.env = Envelope(5, 6)
        self.assertEqual(self.env.a, 5)
        self.assertEqual(self.env.b, 6)

    def test_except_side_type_error(self):
        self.env1 = Envelope('a', 4)

    def test_except_side_less_zero(self):
        with self.assertRaises(ValueError):
            self.env1 = Envelope(-2, 5)
            self.env2 = Envelope(2, -5)
            self.env3 = Envelope(-2, -5)

    def test_compare_envelopes(self):
        self.env1 = Envelope(7, 8)
        self.env2 = Envelope(3, 4)
        self.assertFalse(self.env1.compare_envelopes(self.env2))
        self.assertTrue(self.env2.compare_envelopes(self.env1))
        self.env1 = Envelope(2, 6)
        self.env2 = Envelope(4, 1)
        self.assertFalse(self.env1.compare_envelopes(self.env2))
        self.assertTrue(self.env2.compare_envelopes(self.env1))
        self.env1 = Envelope(3, 4)
        self.env2 = Envelope(5, 7)
        self.assertTrue(self.env1.compare_envelopes(self.env2))
        self.assertFalse(self.env2.compare_envelopes(self.env1))
        self.env1 = Envelope(6, 3)
        self.env2 = Envelope(4, 9)
        self.assertTrue(self.env1.compare_envelopes(self.env2))
        self.assertFalse(self.env2.compare_envelopes(self.env1))
        self.env1 = Envelope(1, 10)
        self.env2 = Envelope(2, 5)
        self.assertFalse(self.env1.compare_envelopes(self.env2))
        self.assertFalse(self.env2.compare_envelopes(self.env1))


if __name__ == '__main__':
    unittest.main(verbosity=2)
