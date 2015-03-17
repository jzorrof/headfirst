__author__ = 'Joe Fan'

import os

def get_dir():
    return os.getcwd()

def change_dir():
    pass

def open_data():
    pass

def close_data():
    pass


if __name__ == '__main__':
    #test field#
    data = open('sketch.txt')
    print(data.readline(), end='')
    print(data.readline(), end='')

    data.seek(0)

    for each_line in data:
        print(data.readline())

    data.seek(0)

    for each_line in data:
        if not each_line.find(':') == -1:
            (role, line_spoken) = each_line.split(':', 1)
            print(role, end='')
            print(' said:', end='')
            print(line_spoken, end='')

    data.close()