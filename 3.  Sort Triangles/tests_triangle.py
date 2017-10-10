import unittest
from triangles2 import Triangle
from triangles2 import NotTriangleError


class TestClassTriangle(unittest.TestCase):
    def test_valid_triangle(self):
        # Arrange
        name = 't1'
        a = 3.0
        b = 4.0
        c = 5.0

        # Act
        t = Triangle(name, a, b, c)

        # Assert
        self.assertEqual(t.name, name)
        self.assertEqual(t.a, a)
        self.assertEqual(t.b, b)
        self.assertEqual(t.c, c)
        self.assertEqual(t.square, 6.0)

    def test_except_side_type_error(self):
        # Assert for exception
        self.assertRaises(TypeError, lambda: Triangle('t1', 2, 3.0, 4.0))
        self.assertRaises(TypeError, lambda: Triangle('t1', 2.0, 3, 4.2))
        self.assertRaises(TypeError, lambda: Triangle('t1', 2.0, 3.3, 4))
        self.assertRaises(TypeError, lambda: Triangle('t1', 2.0, 'b', 4.4))
        self.assertRaises(TypeError, lambda: Triangle('t1', 2.0, 3.5, 'c'))
        self.assertRaises(TypeError, lambda: Triangle('t1', 'a', 3.0, 4.0))

    def test_except_side_less_zero(self):
        # Assert for exception
        self.assertRaises(ValueError, lambda: Triangle('t1', -2.0, 3.0, 4.0))
        self.assertRaises(ValueError, lambda: Triangle('t1', 2.0, -3.0, 4.2))
        self.assertRaises(ValueError, lambda: Triangle('t1', 2.0, 3.3, -4.0))
        self.assertRaises(ValueError, lambda: Triangle('t1', -2.5, -3.8, 4.4))
        self.assertRaises(ValueError, lambda: Triangle('t1', -2.5, 3.5, -4.5))
        self.assertRaises(ValueError, lambda: Triangle('t1', 2.2, -3.2, -4.2))
        self.assertRaises(ValueError, lambda: Triangle('t1', -2.8, -3.8, -4.8))

    def test_except_not_triangle(self):
        # Assert for exception
        self.assertRaises(NotTriangleError, lambda: Triangle('t1', 1.0, 2.0, 3.0))
        self.assertRaises(NotTriangleError, lambda: Triangle('t1', 2.0, 5.0, 1.0))
        self.assertRaises(NotTriangleError, lambda: Triangle('t1', 7.0, 2.0, 3.0))

    def test_sort_square(self):
        #  Arrange
        list_triangles = list()
        self.t1 = Triangle('t1', 3.0, 4.0, 5.0)   # square = 6.0
        list_triangles.append(self.t1)
        self.t2 = Triangle('t2', 4.0, 5.0, 6.0)   # square = 9.92
        list_triangles.append(self.t2)
        self.t3 = Triangle('t3', 5.0, 2.0, 4.0)   # square = 3.8
        list_triangles.append(self.t3)
        # list with triangles in position of decreasing square
        sort_list = [self.t2, self.t1, self.t3]

        # Act
        list_triangles.sort(key=lambda x: x.square, reverse=True)

        # Assert
        self.assertListEqual(list_triangles, sort_list)


if __name__ == '__main__':
    unittest.main(verbosity=2)
