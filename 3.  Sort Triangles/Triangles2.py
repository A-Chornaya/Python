import math


class Triangle:
    def __init__(self, name, a: float, b: float, c: float):
        if a <= 0 or b <= 0 or c <= 0:
            raise ValueError
        # check for sides of triangle
        if a >= b + c \
                or b >= a + c \
                or c >= a + b:
            raise NotTriangleError
        self.__name = name
        self.__a = a
        self.__b = b
        self.__c = c
        self.__square = 1 / 4 * math.sqrt(4 * a * a * b * b -
                                          (a * a + b * b - c * c) ** 2)

    @property
    def name(self):
        return self.__name

    @property
    def a(self):
        return self.__a

    @property
    def b(self):
        return self.__b

    @property
    def c(self):
        return self.__c

    @property
    def square(self):
        return self.__square


class NotTriangleError(Exception):
    pass


if __name__ == '__main__':
    list_of_triangles = list()
    while True:
        tringle_str = input('Enter a triangle:')
        temp_list = tringle_str.split(',', 4)
        if len(temp_list) != 4:
            print('Incorrect input data. Enter data separeted by ","')
            continue
        try:
            t = Triangle(temp_list[0], float(temp_list[1]), float(temp_list[3]),
                         float(temp_list[2]))
            list_of_triangles.append(t)
        except ValueError:
            print('Error of value types. Sides of the triangle must be '
                  'positive numbers')
            continue
        except NotTriangleError:
            print('This sides don`t form a triangle')
            continue

        answer = input('Do you want enter another one? (enter "y" or "yes" if '
                       'want):')
        if answer.lower() == 'y' or answer.lower() == 'yes':
            continue
        break

    list_of_triangles.sort(key=lambda x: x.square, reverse=True)
    print('=======Sort triangles=======')
    for obj in list_of_triangles:
        print('[Triangle %s]: %f cm' % (obj.name, obj.square))
