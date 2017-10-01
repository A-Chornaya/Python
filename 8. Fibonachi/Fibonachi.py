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


print('====Fibonachi in the range====')
try:
    k = int(input('start value:'))
    n = int(input('end value:'))
    if n < 0:
        raise IndexError
    if n <= k:
        raise IndexError
except ValueError:
    print('Error of value type. Please, enter the natural number')
except IndexError:
    print('Wrong value. End must be greater than 0 and Start')
else:
    fibo = fibonachi(n)
    start = find_start(k, fibo)
    fibo_part = fibo[start:len(fibo)]
    print(', '.join(str(e) for e in fibo_part))
