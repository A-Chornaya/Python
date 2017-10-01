import math

def numb_seq(n):
    sequence = [0]
    for i in range(1, int(math.sqrt(n)) + 1):
        sequence.append(i)
    if i**2 == n:
        sequence.pop()
    print(sequence)


try:
    n = int(input('Enter n:'))
except ValueError:
    print('Error of value type. Please, enter a natural number')
else:
    if n >= 0:
        numb_seq(n)
    else:
        print('Number is less than 0. Please, enter a natural number')
