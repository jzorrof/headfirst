'''This is the standard way to include
'''
def print_lol(the_list):
    '''
    print nester list item
    '''
    for each_item in the_list:
        if isinstance(each_item, list):
            print_lol(each_item)
        else:
            print(each_item)