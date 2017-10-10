import sys

def moscow_ticket(str):
    part1 = int(str[0]) + int(str[1]) + int(str[2])
    part2 = int(str[3]) + int(str[4]) + int(str[5])
    if part1 == part2:
        return True
    else:
        return False


def stPeter_ticket(str):
    even = 0
    uneven = 0
    for s in str:
        s_int = int(s)
        if s_int % 2 == 0:
            even += s_int
        else:
            uneven += s_int
    if even == uneven:
        return True
    else:
        return False


try:
    ticket = input('Your ticket:')
    #checking for exception
    number = int(ticket)
    if len(ticket) != 6:
        raise ValueError

    mode = int(input('Mode: 1 - Moscow, 2 - StPetersburg:'))
    if mode == 1:
        result = moscow_ticket(ticket)
    elif mode == 2:
        result = stPeter_ticket(ticket)
    else:
        print('Uncorrect mode')
        sys.exit(1)
except ValueError:
    print('Error of input type')
    sys.exit(1)
else:
    if result:
        print('Congratulation! Your ticket is Happy.')
    else:
        print('Sorry, you ticket isn`t happy :(')
