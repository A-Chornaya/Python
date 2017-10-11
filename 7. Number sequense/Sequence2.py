import sys
import math

def numb_seq(n):
    # Validation
    if type(n) != int:
        raise ValueError
    if n <= 0:
        raise NotPositiveNumberError

    sequence = [0]
    for i in range(1, int(math.sqrt(n)) + 1):
        sequence.append(i)
    # remove last, if square of i = n (not < n)
    if i**2 == n:
        sequence.pop()

    return sequence


class NotPositiveNumberError(Exception):
    pass


class InvalidParameters(Exception):
    pass


if __name__ == '__main__':
    try:
        if len(sys.argv) != 2:
            raise InvalidParameters
        n = int(sys.argv[1])
        seq = numb_seq(n)
        print(', '.join(str(e) for e in seq))
    except InvalidParameters:
        print('Invalid number of parameters. Please, start program as: '
              'name_of file n')
    except ValueError:
        print('Error of value type. Please, enter a natural number')
    except NotPositiveNumberError:
        print('Number is equals or less than 0. Please, enter a natural number')
