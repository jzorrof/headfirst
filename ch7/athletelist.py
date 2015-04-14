
class AthleteList(list):
    """docstring for Athlete"""
    def __init__(self, a_name, a_dob=None, a_times=[]):
        self.name = a_name
        self.dob = a_dob
        self.extend(a_times)

    @property
    def top3(self):
        return (sorted(set(self.sanitize(t) for t in self))[0:3])
    
    @staticmethod
    def sanitize(time_string):
        if '-' in time_string:
            spliter = '-'
        elif ':' in time_string:
            spliter = ':'
        else:
            return(time_string)

        (min, secs) = time_string.split(spliter)
        return (min + '.' + secs)

    @property
    def clean(self):
        return (sorted(set(self.sanitize(t) for t in self)))