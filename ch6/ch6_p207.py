import os

class Athlete(list):
	"""docstring for Athlete"""
	def __init__(self, a_name, a_dob=None, a_times=[]):
		self.name = a_name
		self.dob = a_dob
		self.extend(a_times)

	def top3(self):
		return (sorted(set(sanitize(t) for t in self))[0:3])

def sanitize(time_string):
    if '-' in time_string:
        spliter = '-'
    elif ':' in time_string:
        spliter = ':'
    else:
        return(time_string)

    (min, secs) = time_string.split(spliter)
    return (min + '.' + secs)

vera = Athlete('Vera Vi')
vera.append('1.33')
vera.extend(['2.31', '2.45', '4.21', '1.45'])
print(vera.top3())