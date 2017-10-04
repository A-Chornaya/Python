import math

class Triangle:
    def __init__(self, name, a: float, b: float, c: float):
        if (a <= 0 or b <= 0 or c <= 0):
            raise ValueError
        # check for sides of triangle
        if (a >= b + c or b >= a + c or c >= a + b):
            raise NotTriangle
        self.name = name
        self.a = a
        self.b = b
        self.c = c
        self.square = 1 / 4 * math.sqrt(4 * a*a * b*b - (a*a + b*b + c*c))

class NotTriangle(Exception):
    pass

list_of_triangles = list()
while True:
    tringle_str = input('Enter a triangle:')
    temp_list = tringle_str.split(',', 4)

    try:
        list_of_triangles.append(Triangle(temp_list[0], float(temp_list[1]),
                float(temp_list[2]), float(temp_list[3])))
    except ValueError:
        print('Error of value types. Sides of the triangle must be '
              'positive numbers')
        continue
    except NotTriangle:
        print('This sides don`t form a triangle')
        continue

    answer = input('Do you want enter another one? (enter "y" or "yes" if '
                   'want):')
    if (answer.lower() == 'y' or answer.lower() == 'yes'):
        continue
    break

list_of_triangles.sort(key=lambda x: x.square, reverse=True)
print('=======Sort triangles=======')
for obj in list_of_triangles:
    print('[Triangle %s]: %f cm' % (obj.name, obj.square))
