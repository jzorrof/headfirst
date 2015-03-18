__author__ ='Joe_Fan'
import os

#not use excaption.
if os.path.exists('sketch.txt'):
    data= open('sketch.txt')
    for each_line in data:
        if not each_line.find(':') == -1:
            (role, line_spoken) = each_line.split(':', 1)
            print(role, end='')
            print(' said:', end='')
            print(line_spoken, end='')
    data.close()
else:
    print('The data file is missing!')

print('\t\t\t\t\t\t\t')
try:
    data = open('sketch.txt')
        
    for each_line in data:
        try:
            (role, line_spoken) = each_line.split(':')
            print(role, end='')
            print(' said', end='')
            print(line_spoken, end='')
        except ValueError:
            pass
except IOError:
    print('The data file is missing!')