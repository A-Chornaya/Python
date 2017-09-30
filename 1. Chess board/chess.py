def board(len, hei):
    s1, s2 = '*', ' '
    for i in range(1, len):
        if i % 2 == 0:
            s1 += '*'
            s2 += ' '
        else:
            s1 += ' '
            s2 += '*'
    for j in range(0, hei):
        if j % 2 == 0:
            print(s1)
        else:
            print(s2)


print('======Chess board======')
flag = True
while flag:
    try:
        lenght = int(input("Enter the length:"))
        height = int(input("Enter the height:"))
    except ValueError:
        print('Error of input type. Please, enter a number')
    else:
        flag = False
        board(lenght, height)
