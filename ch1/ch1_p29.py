__author__ = 'Joe Fan'

movies= ["The Holy Grail", 1975, "Terry Jones & Terry Gilliam", 91,
            ["Graham Chapman",["Michael palin", "John Cleese",
                    "Terry Gilliam", "Eric Idle", "Terry Jones"]]]

def print_lol(the_list):
    for each_item in the_list:
        if isinstance(each_item, list):
            print_lol(each_item)
        else:
            print(each_item)

print print_lol(movies)