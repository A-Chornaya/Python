import sys
import os

def find(file_path, str_find):
    find_count = 0
    try:
        with open(file_path) as f:
            for line in f:
                find_count += line.count(str_find)
        return find_count
    except FileNotFoundError:
        print('File "%s" not found' % file_path)
        return 0
    except Exception as e:
        print('Error:', e)



def replace(file_path, str_find, str_replace):
     try:
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
        count_str = find(sys.argv[1], sys.argv[2])
        if count_str:
            print('A string "%s" contained in the file "%s" %i times' %
                  (sys.argv[2], sys.argv[1], count_str))
    else:
        if replace(sys.argv[1], sys.argv[2], sys.argv[3]):
            print('A string "%s" replaced in the file "%s" by a string "%s"' %
                  (sys.argv[2], sys.argv[1], sys.argv[3]))


main()
