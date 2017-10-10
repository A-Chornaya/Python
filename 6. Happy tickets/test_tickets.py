import unittest
from tickets import happy_ticket
from tickets import NotNumberError
from tickets import NotTicketError


class TestClassTickets(unittest.TestCase):
    def test_valid_happy_ticket(self):
        # Arrange
        ticket1 = '028136'
        ticket2 = '276320'
        ticket3 = '456123'
        mode_m = '1'
        mode_p = '2'

        # Act and Assert
        self.assertTrue(happy_ticket(ticket1, mode_m))
        self.assertTrue(happy_ticket(ticket2, mode_p))
        self.assertFalse(happy_ticket(ticket1, mode_p))
        self.assertFalse(happy_ticket(ticket2, mode_m))
        self.assertFalse(happy_ticket(ticket3, mode_m))
        self.assertFalse(happy_ticket(ticket3, mode_p))

    def test_invalid_ticket(self):
        # Assert for exception
        self.assertRaises(TypeError, lambda: happy_ticket(123456, '1'))
        self.assertRaises(TypeError, lambda: happy_ticket(2.3, '2'))
        self.assertRaises(TypeError, lambda: happy_ticket('123456', 1))
        self.assertRaises(TypeError, lambda: happy_ticket('123456', 2.0))
        self.assertRaises(TypeError, lambda: happy_ticket(True, '1'))
        self.assertRaises(TypeError, lambda: happy_ticket('123456', False))

    def test_invalid_value_of_mode(self):
        # Assert for exception
        self.assertRaises(ValueError, lambda: happy_ticket('654321', '0'))
        self.assertRaises(ValueError, lambda: happy_ticket('654321', 'moscow'))

    def test_ticket_string_not_number(self):
        # Assert for exception
        self.assertRaises(NotNumberError, lambda: happy_ticket('Hello', '1'))
        self.assertRaises(NotNumberError, lambda: happy_ticket('-256789', '2'))

    def test_ticket_has_not_6_digits(self):
        # Assert for exception
        self.assertRaises(NotTicketError, lambda: happy_ticket('123', '1'))
        self.assertRaises(NotTicketError, lambda: happy_ticket('01234567', '2'))

    def test_int_to_str_format(self):
        # Arrange
        ticket = 3145

        # Act
        str_ticket = str('{:06}'.format(ticket))

        # Assert
        self.assertEqual(str_ticket, '003145')


if __name__ == '__main__':
    unittest.main(verbosity=2)
