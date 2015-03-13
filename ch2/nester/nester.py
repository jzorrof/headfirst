'''This is the standard way to include
'''
def print_lol(the_list, level=0):
    '''
    print nester list item
    '''
    for each_item in the_list:
        if isinstance(each_item, list):
            print_lol(each_item)
        else:
            for tab_tag in range(level):
                print('\t', end='')
            print(each_item)