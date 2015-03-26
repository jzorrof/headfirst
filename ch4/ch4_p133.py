__author__ ='Joe_Fan'
import os, nester, sys
import pickle

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
    with open('man_data.txt','wb') as man_file:
        #use pickle
        pickle.dump(man, man_file)
    with open('other_data.txt', 'wb') as data_file:
        #use pickle
        pickle.dump(man, data_file)
except IOError as err:
    print("File error: " + str(err))
except pickle.PickleError as perr:
    print("PickleError:" + str(perr))

#test pickleload

try:
    with open('man_data.txt', 'rb') as man_file:
        new_file = pickle.load(man_file)
        print(new_file)
except IOError as e:
    raise e
except pickle.PickleError as pe:
    raise pe
