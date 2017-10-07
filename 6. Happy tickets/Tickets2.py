def happy_ticket(ticket: str, mode: str):
    if mode == '1':   # Moscow mode
        part1 = int(ticket[0]) + int(ticket[1]) + int(ticket[2])
        part2 = int(ticket[3]) + int(ticket[4]) + int(ticket[5])
    else:           # Saint Petersburg mode
        part1 = int(ticket[0]) + int(ticket[2]) + int(ticket[4])
        part2 = int(ticket[1]) + int(ticket[3]) + int(ticket[5])

    if part1 == part2:
        return True
    else:
        return False


def main():
    mode = 0
    try:
        file_path = input('Enter a path for file with mode:')
        with open(file_path, 'r') as f:
            mode = f.readline()
        if mode != '1' and mode != '2':
            raise TypeError('Incorrect type of mode: it must be 1 or 2')
    except FileNotFoundError:
        print('File %s not found' % file_path)
    except ValueError:
        print('Error of value type')
    except TypeError as e:
        print(e)
    else:
        ticket = 0
        count = 0
        while ticket < 1000000:
            str_ticket = str('{:06}'.format(ticket))
            if happy_ticket(str_ticket, mode):
                count += 1
            ticket += 1
        print('Count of happy tickets is:', count)

main()
