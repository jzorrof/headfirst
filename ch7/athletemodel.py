import pickle
from athletelist import AthleteList

def get_coach_data(filename):
    pass

def put_to_store(files_list):
    all_athletes = {}

    for each_file in files_list:
        ath = get_coach_data(each_file)
        all_athletes[ath.name] = ath