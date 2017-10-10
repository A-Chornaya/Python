import unittest
from envelopes2 import Envelope
from envelopes2 import restart_program

class TestClassEnvelope(unittest.TestCase):
    def test_valid_envelope(self):
        # Arrange
        a = 5.0
        b = 6.0

        # Act
        env = Envelope(a, b)

        # Assert
        self.assertEqual(env.a, a)
        self.assertEqual(env.b, b)

    def test_except_side_type_error(self):
        # Assert for exception
        self.assertRaises(TypeError, lambda: Envelope(2, 4.0))
        self.assertRaises(TypeError, lambda: Envelope(6.0, 4))
        self.assertRaises(TypeError, lambda: Envelope('a', 4.0))
        self.assertRaises(TypeError, lambda: Envelope(6.0, 'b'))
        self.assertRaises(TypeError, lambda: Envelope(True, 4.0))
        self.assertRaises(TypeError, lambda: Envelope(6.0, False))

    def test_except_side_less_zero(self):
        # Assert for exception
        self.assertRaises(ValueError, lambda: Envelope(-2.0, 5.0))
        self.assertRaises(ValueError, lambda: Envelope(2.0, -5.0))
        self.assertRaises(ValueError, lambda: Envelope(-2.0, -5.0))

    def test_compare_envelopes(self):
        # Arrange
        env1 = Envelope(7.0, 8.0)
        env2 = Envelope(3.0, 4.0)
        env3 = Envelope(2.0, 6.0)
        env4 = Envelope(4.0, 1.0)
        env5 = Envelope(6.0, 3.0)
        env6 = Envelope(4.0, 9.0)

        #Act and Assert
        self.assertFalse(env1.compare_envelopes(env2))
        self.assertTrue(env2.compare_envelopes(env1))
        self.assertFalse(env3.compare_envelopes(env2))
        self.assertTrue(env4.compare_envelopes(env1))
        self.assertTrue(env2.compare_envelopes(env1))
        self.assertFalse(env1.compare_envelopes(env2))
        self.assertTrue(env5.compare_envelopes(env6))
        self.assertFalse(env6.compare_envelopes(env5))
        self.assertFalse(env2.compare_envelopes(env3))
        self.assertFalse(env3.compare_envelopes(env2))

    def test_func_restart_program(self):
        # Assert
        self.assertTrue(restart_program('y'))
        self.assertTrue(restart_program('Y'))
        self.assertTrue(restart_program('yes'))
        self.assertTrue(restart_program('YES'))
        self.assertTrue(restart_program('Yes'))
        self.assertFalse(restart_program('no'))
        self.assertFalse(restart_program('0'))
        self.assertFalse(restart_program('g'))
        self.assertFalse(restart_program(''))


if __name__ == '__main__':
    unittest.main(verbosity=2)
