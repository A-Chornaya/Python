import sys

def fibonachi(n):
    a, b = 0, 1
    fibo = [a]
    while b <= n:
        fibo.append(b)
        a, b = b, a + b
    return fibo


def find_start(k, fibo):
    i = 0
    while fibo[i] < k:
        i += 1
    return i


if len(sys.argv) != 3:
    print(
        'Invalid number of parameters.'
        '\nPlease, start program as: name_of_file start_value end_value')
    sys.exit(1)

try:
    k = int(sys.argv[1])
    n = int(sys.argv[2])
    if n < 0:
        raise IndexError
    if n <= k:
        raise IndexError
except ValueError:
    print('Error of value type. Please, enter the natural number')
except IndexError:
    print('Wrong value. End must be greater than 0 and Start')
else:
    print('====Fibonachi in the range====')
    fibo = fibonachi(n)
    start = find_start(k, fibo)
    fibo_part = fibo[start:len(fibo)]
    print(', '.join(str(e) for e in fibo_part))
