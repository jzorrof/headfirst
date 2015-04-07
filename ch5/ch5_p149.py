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

try:
    with open('james.txt', 'r') as jaf:
        data = jaf.readline()
        james = data.strip().split(',')

    with open('julie.txt') as juf:
    	data = juf.readline()
    	julie = data.strip().split(',')

    with open("mikey.txt") as mif:
    	data = mif.readline()
    	mikey = data.strip().split(',')

    with open("sarah.txt") as saf:
    	data = saf.readline()
    	sarah = data.strip().split(',')
except IOError as e:
    raise e

james_clean =[]
julie_clean =[]
mikey_clean =[]
sarah_clean =[]

for each_item in james:
    james_clean.append(sanitize(each_item))
for each_item in julie:
    julie_clean.append(sanitize(each_item))
for each_item in mikey:
    mikey_clean.append(sanitize(each_item))
for each_item in sarah:
    sarah_clean.append(sanitize(each_item))

print(sorted(james_clean))
print(sorted(julie_clean))
print(sorted(mikey_clean))
print(sorted(sarah_clean))