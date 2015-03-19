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
    os.chdir("../")
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

    data.seek(0)
    #p93 try catch excepion
    for each_line in data:
        try:
            (role, line_spoken) = each_line.split(':')
            print(role, end='')
            print(' said:', end='')
            print(line_spoken, end='')
        except:
            pass

    data.close()