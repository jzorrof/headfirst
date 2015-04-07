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

# try:
#     with open('james.txt', 'r') as jaf:
#         data = jaf.readline()
#         james = data.strip().split(',')

#     with open('julie.txt') as juf:
#     	data = juf.readline()
#     	julie = data.strip().split(',')

#     with open("mikey.txt") as mif:
#     	data = mif.readline()
#     	mikey = data.strip().split(',')

#     with open("sarah.txt") as saf:
#     	data = saf.readline()
#     	sarah = data.strip().split(',')
# except IOError as e:
#     raise e

def get_coach_data(filename):
    try:
        with open(filename) as f:
            data = f.readline()
            return(data.strip().split(','))
    except IOError as e:
        print('file error: ' + str(e))
        return(None)

# james_clean =[]
# julie_clean =[]
# mikey_clean =[]
# sarah_clean =[]

# for each_item in james:
#     james_clean.append(sanitize(each_item))
# for each_item in julie:
#     julie_clean.append(sanitize(each_item))
# for each_item in mikey:
#     mikey_clean.append(sanitize(each_item))
# for each_item in sarah:
#     sarah_clean.append(sanitize(each_item))
james = get_coach_data('james.txt')
julie = get_coach_data('julie.txt')
mikey = get_coach_data('mikey.txt')
sarah = get_coach_data('sarah.txt')

# james = sorted(sanitize(t) for t in james)
# julie = sorted(sanitize(t) for t in julie)
# mikey = sorted(sanitize(t) for t in mikey)
# sarah = sorted(sanitize(t) for t in sarah)

# unique_james = []
# unique_julie = []
# unique_mikey = []
# unique_sarah = []

# for item in james:
#     if item not in unique_james:
#         unique_james.append(item)

# for item in julie:
#     if item not in unique_julie:
#         unique_julie.append(item)


# for item in mikey:
#     if item not in unique_mikey:
#         unique_mikey.append(item)

# for item in sarah:
#     if item not in unique_sarah:
#         unique_sarah.append(item)

# print(unique_james[0:3])
# print(unique_julie[0:3])
# print(unique_mikey[0:3])
# print(unique_sarah[0:3])


'''
add a set demo
set() 工厂方法
'''
print(sorted(set(sanitize(t) for t in james))[0:3])
print(sorted(set(sanitize(t) for t in julie))[0:3])
print(sorted(set(sanitize(t) for t in mikey))[0:3])
print(sorted(set(sanitize(t) for t in sarah))[0:3])