def translit(numb):
    result_str = ''

    units = ('ноль', 'один', 'два', 'три', 'четыре', 'пять', 'шесть', 'семь',
             'восемь', 'девять')
    second_dozen = ('десять', 'одиннадцать', 'двенадцать', 'тринадцать',
                    'четырнадцать', 'пятнадцать', 'шестнадцать', 'семнадцать',
                    'восемнадцать', 'девятнадцать')
    dozens = ('двадцать', 'тридцать', 'сорок', 'пятьдесят',
              'шестьдесят', 'семьдесят', 'восемьдесят', 'девяносто')
    hundreds = ('сто', 'двести', 'триста', 'четыреста', 'пятьсот', 'шестьсот',
                'семьсот', 'восемьсот', 'девятьсот')
    thousands = ('тысяча', 'тысячи', 'тысяч')
    other = ('тысяч', 'миллион', 'миллиард', 'триллион', 'квадриллион',
             'квинтиллион', 'секстиллион', 'сеплиллион', 'октиллион',
             'нониллион', 'дециллион')
    suffix = ('а', 'ов', 'и')

    if numb == 0:
        result_str = units[numb]

    flag_negative = False
    if numb < 0:
        numb = numb * -1
        flag_negative = True

    j = -1      # increment for number classes
    while numb >= 1:
        one_class = numb % 1000

        # transform one class of number to string
        temp_str = ''
        whole = one_class // 100
        part = one_class % 100
        part2 = 0
        if whole > 0:
            temp_str = temp_str + hundreds[whole - 1] + ' '
        if part >= 20:
            part1 = part // 10
            part2 = part % 10
            temp_str = temp_str + dozens[part1 - 2] + ' '
            if part2 != 0:
                temp_str = temp_str + units[part2] + ' '
        elif 10 <= part <= 19:
            temp_str = temp_str + second_dozen[part - 10] + ' '
        elif 0 < part <= 9:
            temp_str = temp_str + units[part] + ' '

        # add prefix if number > 999
        if j >= 0 and one_class > 0:
            temp_str = temp_str + other[j]

        # add suffixes
        # replace 'один тысяч'
        if j == 0 and (part == 1 or part2 == 1):
            temp_str = temp_str[:len(temp_str)-10] + 'одна тысяча'
        # replace 'два тысяч'
        if j == 0 and (part == 2 or part2 == 2):
            temp_str = temp_str[:len(temp_str)-9] + 'две тысячи'
        # for thousands from 3 to 4
        if j == 0 and (2 < part < 5 or 2 < part2 < 5):
            temp_str = temp_str + suffix[2]
        # for millions and higher from 2 to 4
        if j > 0 and (1 < part < 5 or 1 < part2 < 5):
            temp_str = temp_str + suffix[0]
        # for millions and higher from 5
        elif j > 0 and (4 < part < 20 or part2 > 4
                        or (one_class > 0 and part % 10 == 0)):
            temp_str = temp_str + suffix[1]

        numb = numb // 1000
        result_str = temp_str + ' ' + result_str
        j += 1

    if flag_negative:
        result_str = 'минус' + result_str

    return result_str


def main():
    try:
        number = int(input('Enter a number:'))
    except ValueError:
        print('Error of input data. Please, enter an integer')
    else:
        try:
            result = translit(number)
        except IndexError:
            print('Number must be less than 9.99e35')
        else:
            print(result)

main()
