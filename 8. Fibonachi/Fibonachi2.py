import sys

def fibonachi(n: int):
    #Validation
    if type(n) != int:
        raise ValueError
    if n < 0:
        raise IndexError

    a, b = 0, 1
    fibo = [a]
    while b <= n:
        fibo.append(b)
        a, b = b, a + b
    return fibo


def find_start(k: int, fibo: list):
    #Validation
    if type(k) != int or type(fibo) != list:
        raise ValueError
    if k >= fibo[len(fibo) - 1]:
        raise IndexError

    i = 0
    while fibo[i] < k:
        i += 1
    return i


if __name__ == '__main__':
    if len(sys.argv) != 3:
        print(
            'Invalid number of parameters.'
            '\nPlease, start program as: name_of_file start_value end_value')
        sys.exit(1)

    try:
        k = int(sys.argv[1])
        n = int(sys.argv[2])
        if n <= k:
            raise IndexError

        print('====Fibonachi in the range====')
        fibo = fibonachi(n)
        start = find_start(k, fibo)
        fibo_part = fibo[start:len(fibo)]
        print(', '.join(str(e) for e in fibo_part))
    except ValueError:
        print('Error of value type. Please, enter the natural number')
    except IndexError:
        print('Wrong value. End must be greater than 0 and Start')
