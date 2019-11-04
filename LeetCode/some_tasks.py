##########################################
# 22
# Напишите программу, которая принимает текст и выводит два слова: наиболее часто встречающееся и самое длинное.
# from collections import Counter
#
# def often_and_long(word_string):
#     words = word_string.split(' ')
#     count = Counter(words)
#     max_common, ocurances = count.most_common(1)[0]
#     longest = max(words, key=len)
#     return max_common, longest
#
# w_str = 'bar mom mother bar belong mom cute bar'
# max_common, longest = often_and_long(w_str)
# print(f'most common = "{max_common}", the longest = "{longest}"')
# most common = "bar", the longest = "mother"

##########################################
# 21
# Нужно проверить, все ли числа в последовательности уникальны.
# def all_nums_unique(nums):
#     return len(nums)  == len(set(nums))
#
# l1 = [1,2,3,4,5]
# l2 = [1,3,3,4,5]
# print(all_nums_unique(l1))      # True
# print(all_nums_unique(l2))      # False

##########################################
# 20
# С помощью анонимной функции извлеките из списка числа, делимые на 15.
# def mul_15(l):
#     return list(filter(lambda x: not x % 15, l))
#
# l = [1, 15, 17, 30, 40]
# print(mul_15(l))

##########################################
# 19
# Поменяйте значения переменных местами.
# x = 15
# y = 7
# x,y = y, x
# print(x, y)

##########################################
# 18
# Посчитайте, сколько раз символ встречается в строке.
# def count_symbol(s_str, symbol):
#     return s_str.count(symbol)
#
# print(count_symbol('abamamama', 'a'))      # 5

##########################################
# 17
# Сложите цифры целого числа.
# def sum_numerals(n):
#     sum = 0
#     while n != 0:
#         n, p = divmod(n, 10)
#         sum += p
#     return sum
#
# print(sum_numerals(123))        # 6
# print(sum_numerals(123456789))  # 45
#
# def sum_digits(n):
#     return sum([int(d) for d in str(n)])
#
# print(sum_digits(123))          # 6
# print(sum_digits(123456789))    # 45

##########################################
# 16
# Выведите список файлов в указанной директории.
# !!!!!!!!!!!!!!!!!!!!!!!!!!

# from os import listdir
# from os.path import isfile, join
# files = [f for f in listdir('C:/Users/achorn/Documents/') if isfile(join('C:/Users/achorn/Documents/', f))]
# print(files)

##########################################
# 15
# Напишите программу, которая принимает два списка и выводит все элементы первого, которых нет во втором.
# def list_sub(l_1, l_2):
#     return set(l_1) - set(l_2)
#
# l_1 = [1,3,5,7,9]
# l_2 = [1,2,3,4,5]
#
# print(list_sub(l_1, l_2))       # {9, 7}

##########################################
# 14
# Напишите программу, которая выводит чётные числа из заданного списка и останавливается, если встречает число 237.
# def even_number(num_list):
#     result = []
#     for n in num_list:
#         if n % 2 == 0:
#             result.append(n)
#         elif n == 237:
#             break
#
#     return result
#
# numbers = [24, 37, 46, 55, 89, 237, 100, 93]
# print(even_number(numbers))       # [24, 46]

##########################################
# 13
# При заданном целом числе n посчитайте n + nn + nnn.
# def mul(n):
#     return n + int(str(n) * 2) + int(str(n) * 3)
#
# def mul_neg(n):
#     res = abs(n) + int(str(abs(n)) * 2) + int(str(abs(n)) * 3)
#     return res if n >= 0 else -res
#
# print(mul(1))       #123
# print(mul_neg(-1))  #-123

##########################################
# 12
# Напишите программу, которая принимает имя файла и выводит его расширение. Если расширение у файла определить невозможно, выбросите исключение.
#  def expansion(name):
#     if '.' in name:
#         return name.split('.')[-1]
#     else:
#         raise ValueError('File has no extension')
#
# print(expansion('1.txt'))       # txt
# print(expansion('1.txt.exe'))   # exe
# print(expansion('1'))           # ValueError: File has no extension

##########################################
# 11
# Выведите первый и последний элемент списка.
# def get_first_last(l):
#     if l:
#         return l[0], l[-1]
#     else:
#         return 'list is empty'
# l = [5,4,3,2,1]
# print(get_first_last(l))                # (5, 1)
# print(get_first_last([]))               # list is empty
# print(f'first: {l[0]}, last: {l[-1]}')  #first: 5, last: 1

##########################################
# 10
# Вы принимаете от пользователя последовательность чисел, разделённых запятой. Составьте список и кортеж с этими числами.
# def str_to_lst_tup(s):
#     list_of_strings = s.split(',')
#     integers = map(int, list_of_strings)
#     lst = list(integers)
#     tup = tuple(lst)
#     return lst, tup
#
# s1 = '1,2,3,4,5'
# print(str_to_lst_tup(s1))

##########################################
# 9
# Сделайте так, чтобы число секунд отображалось в виде дни:часы:минуты:секунды.
# def sec_to_date(seconds):
#     days = seconds // (24 * 3600)
#     seconds %= 24 * 3600
#     hours = seconds // 3600
#     seconds %= 3600
#     minutes = seconds // 60
#     seconds %= 60
#     print(f'{days}:{hours}:{minutes}:{seconds}')
#
# sec_to_date(1234567)

##########################################
# 8
# Напишите проверку на то, является ли строка палиндромом. Палиндром — это слово или фраза, которые одинаково читаются слева направо и справа налево.
# def check_polindrom(s):
#     return s == ''.join(reversed(s))
#
# print(check_polindrom('qweewq'))
##########################################
# 7
'''
Нужно вывести первые n строк треугольника Паскаля.
В этом треугольнике на вершине и по бокам стоят единицы,
а каждое число внутри равно сумме двух расположенных над ним чисел.
'''
# def pascal_triangle(n):
#     triangle = list()
#     # triangle.append([1])
#     for i in range(1, n+1):
#         new_row = list()
#         for j in range(i):
#             if j == 0 or j == i-1:
#                 new_row.append(1)
#             else:
#                 new_row.append(triangle[i-2][j-1] + triangle[i-2][j])
#         if new_row:
#             triangle.append(new_row)
#     return triangle
#
# my_triangle = pascal_triangle(10)
# for line in my_triangle:
#     print(line)
##########################################
# 6
# Напишите код, который переводит целое число в строку, при том что его можно применить в любой системе счисления.
# print(int('ABC', 16))

##########################################
# 5
# Найдите три ключа с самыми высокими значениями в словаре
# import operator
# my_dict = {'a':500, 'b':5874, 'c': 560,'d':400, 'e':5874, 'f': 20}
#
# max_keys = max(my_dict.items(), key=operator.itemgetter(1))
# print(max_keys)         # ('b', 5874)
#
# #answer
# from heapq import nlargest
# result = nlargest(3, my_dict, key=my_dict.get)
# print(result)           # ['b', 'e', 'c']
##########################################
# 4
# Напишите программу для слияния нескольких словарей в один.
# d1 = {'a':'a1', 'b': 'b1'}
# d2 = {'c':'c2', 'b': 'b2'}
# d3 = {'d':'d3', 'e': 'e3'}
#
# from collections import ChainMap
# d = ChainMap(d1, d2, d3)
# print(d)            # ChainMap({'a': 'a1', 'b': 'b1'}, {'c': 'c2', 'b': 'b2'}, {'d': 'd3', 'e': 'e3'})
# d_common = dict(d)
# print(d_common)     # {'d': 'd3', 'e': 'e3', 'c': 'c2', 'b': 'b1', 'a': 'a1'}
# # ключ b с первым найденным значением
# d_common_2 = {**d1, **d2, **d3}
# print(d_common_2)   # {'a': 'a1', 'b': 'b2', 'c': 'c2', 'd': 'd3', 'e': 'e3'}
# # ключ b с первым найденным значением

##########################################
# 3
# Отсортируйте словарь по значению в порядке возрастания и убывания.
# import operator
# my_dict = {'a':500, 'b':5874, 'c': 560,'d':400, 'e':5874, 'f': 20}
#
# dict_small = sorted(my_dict.items(), key=operator.itemgetter(1))
# print(dict_small)   # [('f', 20), ('d', 400), ('a', 500), ('c', 560), ('b', 5874), ('e', 5874)]
# dict_big = sorted(dict_small, key=lambda x: x[1], reverse=True)
# print(dict_big)     # [('b', 5874), ('e', 5874), ('c', 560), ('a', 500), ('d', 400), ('f', 20)]

##########################################
# 2
# Даны списки:
# a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89];
# b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13].
# Нужно вернуть список, который состоит из элементов, общих для этих двух списков.
# a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89];
# b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
# intersection_list = list(set(a) & set(b))
# print(intersection_list)        # [1, 2, 3, 5, 8, 13]
# # для сохранения дублей
# common_list = list(filter(lambda elem: elem in b, a))
# print(common_list)              # [1, 1, 2, 3, 5, 8, 13]

##########################################
# 1
# Есть список a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89].
# Выведите все элементы, которые меньше 5.
# a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
# res = [elem for elem in a if elem < 5]
# print(res)          # [1, 1, 2, 3]