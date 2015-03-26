__author__='Joe_Fan'

import os

try:
    with open('james.txt', 'r') as jaf:
        data = jaf.readline()
        james = data.strip().split(',')
except Exception, e:
    raise e
finally:
    print james