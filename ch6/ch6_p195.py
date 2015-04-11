__author__='Joe_Fan'

import os

class Athlete:
    """docstring for Athlete"""
    def __init__(self, a_name, a_dob=None, a_times=[]):
        self.name = a_name
        self.dob = a_dob
        self.times = a_times

    def top3(self):
         return (sorted(set([sanitize(t) for t in self.times]))[0:3])

    def add_time(self, value_time):
        self.times.append(value_time)

    def add_times(self, list_times):
        self.times.extend(list_times)

def sanitize(time_string):
    if '-' in time_string:
        spliter = '-'
    elif ':' in time_string:
        spliter = ':'
    else:
        return(time_string)

    (min, secs) = time_string.split(spliter)
    return (min + '.' + secs)


def get_coach_data(filename):
    try:
        with open(filename) as f:
            data = f.readline()
        temple = data.strip().split(',')
        # return({'NAME': temple.pop(0),
        #         'DOB': temple.pop(0),
        #         'TIME': str(sorted(set([sanitize(t) for t in temple]))[0:3])})
        return (Athlete(temple.pop(0), temple.pop(0), temple))
    except IOError as e:
        print('file error: ' + str(e))
        return(None)

james = get_coach_data('james2.txt')
print(james.name + "'s fastest times are: " + \
        str(james.top3()))

vera = Athlete('Vera Vi')
vera.add_time('1.12')
print(vera.top3())
vera.add_times(['2.31', '2.41', '2.62'])
print(vera.top3())


