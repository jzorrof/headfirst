__author__ ='Joe_Fan'
import os, nester, sys

def print_lol(the_list, intent=False, level=0, fn=sys.stdout):
    '''
    print nester list item
    '''
    for each_item in the_list:
        if isinstance(each_item, list):
            print_lol(each_item, intent, level+1, fn)
        else:
            if intent:
                for tab_tag in range(level):
                    print('\t', end='', file=fn )
            print(each_item, file=fn)
os.chdir('../')

man = []
other = []
try:
    data = open('sketch.txt')
    for each_line in data:
        try:
            (role, line_spoken) = each_line.split(':',1)
            line_spoken = line_spoken.strip() 
            if role =='Man':
                man.append(line_spoken)
            elif role == 'Other Man':
                other.append(line_spoken)
        except ValueError:
            pass

except IOError:
    print('The data file is missing!', end='')
    
try:
    with open('man_data.txt','w') as man_file:
        #print(man, file=man_file)
        print_lol(man, fn=man_file);
    with open('other_data.txt', 'w') as data_file:
        #print(other, file=data_file)
        print_lol(other, fn=data_file)
except IOError as err:
    print("File error: " + str(err))