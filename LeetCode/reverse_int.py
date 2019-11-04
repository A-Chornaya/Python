# Given a 32-bit signed integer, reverse digits of an integer.

def reverse_1(x: int) -> int:
    negative = False
    result = 0
    if x < 0:
        negative = True
        x *= -1

    while x != 0:
        tmp = result * 10 + x % 10
        result = tmp
        x = x // 10

    if negative:
        result *= -1

    return result if (-2) ** 31 <= result <= 2 ** 31 - 1 else 0

def reverse_2(x: int) -> int:
    tmp = str(x)
    if '-' in tmp:
        tmp = tmp[1:]
        tmp = '-' + tmp[::-1]
    else:
        tmp = tmp[::-1]
    result = int(tmp)
    if (-2) ** 31 <= result <= 2 ** 31 - 1:
        return result
    else:
        return 0

def reverse_3(x: int) -> int:
    result = int(str(x)[::-1]) if x > 0 else -int(str(-x)[::-1])
    return result if (-2) ** 31 <= result <= 2 ** 31 - 1 else 0

print(reverse_1(123))           # 321
print(reverse_2(-123))          # 321
print(reverse_3(987654321))     # 123456789
