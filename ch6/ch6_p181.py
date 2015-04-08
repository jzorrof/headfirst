__author__='Joe_Fan'

import os

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
            return(data.strip().split(','))
    except IOError as e:
        print('file error: ' + str(e))
        return(None)

sarah = get_coach_data('sarah2.txt')
# (sarah_name, sarah_dob) = sarah.pop(0), sarah.pop(0)
# print(sarah_name + "'s fastest times are: " + \
# 	str(sorted(set([sanitize(t) for t in sarah]))[0:3]))
sarah_data = {}
sarah_data['name'] = sarah.pop(0)
sarah_data['dob'] = sarah.pop(0)
sarah_data['time'] = sarah
print(sarah_data['name'] + "'s fastest times are: " + \
        str(sorted(set([sanitize(t) for t in sarah]))[0:3]))

