__author__ = 'joe_fan'

cast = ["The Holy Grail", "The Life of Brian", "The Meaning of life"]

# insert year
cast.insert(1, 1975)
cast.insert(3, 1979)
cast.append(1983)
print(cast)
# create new list
cast_new = ["The Holy Grail", 1975,
            "The Life of Brian", 1979,
            "The Meaning of life", 1983]

print(cast_new)