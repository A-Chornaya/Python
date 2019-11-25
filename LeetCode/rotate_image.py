"""
You are given an n x n 2D matrix representing an image. Rotate the image by 90 degrees (clockwise).

Note:
You have to rotate the image in-place, which means you have to modify the input 2D matrix directly. DO NOT allocate another 2D matrix and do the rotation.

Example:
Given input matrix =
[
  [1,2,3],
  [4,5,6],
  [7,8,9]
],
rotate the input matrix in-place such that it becomes:
[
  [7,4,1],
  [8,5,2],
  [9,6,3]
]

Do not return anything, modify matrix in-place instead.
"""

def rotate(matrix):
    i = 0
    n = len(matrix) - 1
    while i < n:
        for k in range(0, n-i):
            a = matrix[i][i + k]
            b = matrix[i + k][n]
            c = matrix[n][n - k]
            d = matrix[n - k][i]
            # b, c, d, a, = a, b, c, d
            matrix[i][i + k] = d
            matrix[i + k][n] = a
            matrix[n][n - k] = b
            matrix[n - k][i] = c
        i += 1
        n -= 1

def print_matrix(matrix):
    for row in range(len(matrix)):
        print(matrix[row])

matrix =[
  [ 5, 1, 9,11],
  [ 2, 4, 8,10],
  [13, 3, 6, 7],
  [15,14,12,16]
]

rotate(matrix)
print_matrix(matrix)
# [15, 13, 2, 5]
# [14, 3, 4, 1]
# [12, 6, 8, 9]
# [16, 7, 10, 11]

matrix_0 = [[]]
rotate(matrix_0)
print_matrix(matrix_0)
# []


matrix_1 = [
    [1,   2,  3,  4,  5,  6,  7],
    [8,   9, 10, 11, 12, 13, 14],
    [15, 16, 17, 18, 19, 20, 21],
    [22, 23, 24, 25, 26, 27, 28],
    [29, 30, 31, 32, 33, 34, 35],
    [36, 37, 38, 39, 40, 41, 42],
    [43, 44, 45, 46, 47, 48, 49]
]

rotate(matrix_1)
print_matrix(matrix_1)
# [43, 36, 29, 22, 15, 8, 1]
# [44, 37, 30, 23, 16, 9, 2]
# [45, 38, 31, 24, 17, 10, 3]
# [46, 39, 32, 25, 18, 11, 4]
# [47, 40, 33, 26, 19, 12, 5]
# [48, 41, 34, 27, 20, 13, 6]
# [49, 42, 35, 28, 21, 14, 7]


###
# if we can use new matrix
matrix_11 =[
  [ 5, 1, 9,11],
  [ 2, 4, 8,10],
  [13, 3, 6, 7],
  [15,14,12,16]
]
matrix_new_1 = [list(reversed(list(i))) for i in zip(*matrix_11)]
print_matrix(matrix_new_1)
# [
#     [15, 13, 2, 5],
#     [14, 3, 4, 1],
#     [12, 6, 8, 9],
#     [16, 7, 10, 11]
# ]

matrix_111 =[
  [ 5, 1, 9,11],
  [ 2, 4, 8,10],
  [13, 3, 6, 7],
  [15,14,12,16]
]
matrix_new_2 = [list(elem) for elem in map(reversed, zip(*matrix_111))]
print_matrix(matrix_new_2)
# [
#     [15, 13, 2, 5],
#     [14, 3, 4, 1],
#     [12, 6, 8, 9],
#     [16, 7, 10, 11]
# ]
