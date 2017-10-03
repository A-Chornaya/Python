import sys

def board(len, hei):
    s1, s2 = '*', ' '
    for i in range(1, len):
        if i % 2 == 0:
            s1 += '*'
            s2 += ' '
        else:
            s1 += ' '
            s2 += '*'
    for j in range(0, hei):
        if j % 2 == 0:
            print(s1)
        else:
            print(s2)


if len(sys.argv) != 3:
    print(
        'Invalid number of parameters.'
        '\nPlease, start program as: name_of_file length height')
    sys.exit(1)

try:
    lenght = int(sys.argv[1])
    height = int(sys.argv[2])
    if (lenght <= 0 or height <= 0):
        raise ValueError
except ValueError:
    print('Error of input type. Please, enter a positive integer')
else:
    print('======Chess board======')
    board(lenght, height)
