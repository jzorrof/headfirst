import pickle
from athletelist import AthleteList

def get_coach_data(filename):
    try:
        with open(filename) as f:
            data = f.readline()
        temple = data.strip().split(',')
        # return({'NAME': temple.pop(0),
        #         'DOB': temple.pop(0),
        #         'TIME': str(sorted(set([sanitize(t) for t in temple]))[0:3])})
        return (AthleteList(temple.pop(0), temple.pop(0), temple))
    except IOError as e:
        print('file error: ' + str(e))
        return(None)

def put_to_store(files_list):
    all_athletes = {}
    for each_file in files_list:
        ath = get_coach_data(each_file)
        all_athletes[ath.name] = ath
    try:
        with open('athletes.pickle', 'wb') as athf:
            pickle.dump(all_athletes, athf)
    except IOError as e:
        print('File error (put_to_store): ' + e)
    return(all_athletes)

def get_from_store():
    all_athletes = {}
    try:
        with open('athletes.pickle', 'rb') as athf:
            all_athletes = pickle.load(athf)
    except Exception as e:
        print('File error (get_from_store): ' + e)
    return(all_athletes)

if __name__ == '__main__':
    the_files= ['james2.txt', 'julie2.txt', 'mikey2.txt', 'sarah2.txt']
    data = put_to_store(the_files)
    print(data)
    data_copy = get_from_store()
    for each_athlete in data_copy:
        print(data_copy[each_athlete].name + ' ' + data_copy[each_athlete].dob)