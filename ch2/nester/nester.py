'''This is the standard way to include
'''
import os, sys

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