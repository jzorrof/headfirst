__author__='Joe_Fan'

import os

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
finally:
    print(james)
    print(julie)
    print(mikey)
    print(sarah)