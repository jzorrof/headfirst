#! /Users/joe_fan/PycharmProjects/headfirst/py3env/bin/python
import athletemodel
import yate
import glob

data_file = glob.glob("data/*.txt")
athletes = athletemodel.put_to_store(data_file)

print(yate.start_response())
print(yate.include_header('Coach Kelly'))
print(yate.start_form('generate_timing_data.py'))
print(yate.para('select'))
for each_athletes in athletes:
    print(yate.radio_button('which_athlete', athletes[each_athletes].name))
print(yate.end_form('Select'))
print(yate.include_footer({"Home":"/index.html"}))