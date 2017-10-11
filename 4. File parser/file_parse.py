import sys
import os


def find(file_path, str_find):
    find_count = 0
    try:
        if type(file_path) != str or type(str_find) != str:
            raise TypeError
        with open(file_path) as f:
            for line in f:
                find_count += line.count(str_find)
        return find_count
    except FileNotFoundError:
        print('File "%s" not found' % file_path)
        return -1
    except TypeError:
        print('Error of Type. File_path and string_to_find must be strings')
    except Exception as e:
        print('Error:', e)
        return -1


def replace(file_path, str_find, str_replace):
    try:
        if type(file_path) != str or type(str_find) != str \
                or type(str_replace) != str:
            raise TypeError
        with open(file_path, 'r') as f:
            with open('temp.txt', 'w') as temp:
                for line in f:
                    line_new = line.replace(str_find, str_replace)
                    temp.write(line_new)
        os.remove(file_path)
        os.rename('temp.txt', file_path)
        return True
    except FileNotFoundError:
        print('File "%s" not found' % file_path)
        return False
    except TypeError:
        print('Error of Type. File_path and string_to_find must be strings')
    except Exception as e:
        print('Error:', e)
    finally:
        if os._exists('temp.txt'):
            os.remove('temp.txt')


def main():
    if len(sys.argv) < 3 or len(sys.argv) > 4:
        print('Wrong number or parameters\n'
              'For search string enter: program_file '
              'your_file string_for_search\n'
              'For replace string enter: program_file '
              'your_file replacement_string new_string')

    elif len(sys.argv) == 3:
        file_name = sys.argv[1]
        str_to_find = sys.argv[2]

        count_str = find(file_name, str_to_find)
        if count_str > 0:
            print('A string "%s" contained in the file "%s" %i times' %
                  (str_to_find, file_name, count_str))
        elif count_str == 0:
            print('There are no string "%s" in a file "%s"' % (str_to_find,
                                                               file_name))
    else:
        file_name = sys.argv[1]
        str_to_find = sys.argv[2]
        str_replace = sys.argv[3]

        count_str = find(file_name, str_to_find)
        if count_str > 0:
            if replace(file_name, str_to_find, str_replace):
                print('A string "%s" replaced in the file "%s" by a string '
                      '"%s" %i times' %
                      (str_to_find, file_name, str_replace, count_str))
        else:
            print('There are no string "%s" for replacement' % str_to_find)

if __name__ == '__main__':
    main()
