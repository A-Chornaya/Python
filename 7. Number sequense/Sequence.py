import math

def numb_seq(n):
    sequence = [0]
    for i in range(1, int(math.sqrt(n)) + 1):
        sequence.append(i)
    # remove last, if square of i = n (not < n)
    if i**2 == n:
        sequence.pop()
    print(', '.join(str(e) for e in sequence))


if len(sys.argv) != 2:
    print(
        'Invalid number of parameters. Please, start program as: name_of_file n')
    sys.exit(1)

try:
    n = int(sys.argv[1])
except ValueError:
    print('Error of value type. Please, enter a natural number')
else:
    if n >= 0:
        numb_seq(n)
    else:
        print('Number is less than 0. Please, enter a natural number')
