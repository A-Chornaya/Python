import unittest
from Triangles2 import *


class TestClassTriangle(unittest.TestCase):
    def test_valid_triangle(self):
        self.t = Triangle('t1', 3, 4, 5)
        self.assertEqual(self.t.name, 't1')
        self.assertEqual(self.t.a, 3)
        self.assertEqual(self.t.b, 4)
        self.assertEqual(self.t.c, 5)
        self.assertEqual(self.t.square, 6.0)

    def test_except_side_less_zero(self):
        with self.assertRaises(ValueError):
            self.t1 = Triangle('t1', 2, 3, 4)
            self.t2 = Triangle('t2', 2, -3, 4)
            self.t3 = Triangle('t3', 2, 3, -4)
            self.t4 = Triangle('t4', -2, -3, 4)
            self.t5 = Triangle('t5', -2, 3, -4)
            self.t6 = Triangle('t6', 2, -3, -4)
            self.t7 = Triangle('t7', -2, -3, -4)

    def test_except_not_triangle(self):
        with self.assertRaises(NotTriangleError):
            self.t1 = Triangle('t1', 1, 2, 3)
            self.t2 = Triangle('t2', 2, 5, 1)
            self.t3 = Triangle('t3', 7, 2, 3)

    def test_sort_square(self):
        list_of_triangles = list()
        self.t1 = Triangle('t1', 3, 4, 5)   # square = 6.0
        list_of_triangles.append(self.t1)
        self.t2 = Triangle('t2', 4, 5, 6)   # square = 9.92
        list_of_triangles.append(self.t2)
        self.t3 = Triangle('t3', 5, 2, 4)   # square = 3.8
        list_of_triangles.append(self.t3)
        list_of_triangles.sort(key=lambda x: x.square, reverse=True)
        # list with triangles in position of decreasing square
        my_list = [self.t2, self.t1, self.t3]
        self.assertListEqual(list_of_triangles, my_list)


if __name__ == '__main__':
    unittest.main(verbosity=2)
