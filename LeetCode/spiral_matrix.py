# Given a positive integer n, generate a square matrix filled with elements from 1 to n2 in spiral order.

def generateMatrix(n):
    matrix = [[0 for j in range(n)] for i in range(n)]
    left = 0            # left index of square
    right = n - 1       # right index of square
    count = 0           # counter for values
    m = n               # length of quare side
    start = 1           # start value for the next inner square

    while left <= right:
        j = right       # for back iteration
        # iteretion by top row of square
        for i in range(left, right):
            matrix[left][i] = count + 1
            matrix[i][right] = count + m
            matrix[right][j] = count + 2 * m - 1
            matrix[j][left] = count + 3 * m - 2
            count += 1
            j -= 1
        count = (start - 1) + 4 * m - 4     # last biggest num in square
        start = count + 1                   # start value for the next inner square
        if left == right:
            matrix[left][left] = start      # the last middle value
        left += 1
        right -= 1
        m -= 2

    return matrix


matrix = generateMatrix(5)
for row in matrix:
    print(row)
'''
[1, 2, 3, 4, 5]
[16, 17, 18, 19, 6]
[15, 24, 25, 20, 7]
[14, 23, 22, 21, 8]
[13, 12, 11, 10, 9]
'''