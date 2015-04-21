#! /Users/joe_fan/PycharmProjects/headfirst/py3env/bin/python

import cgi
import athletemodel
import yate

athletes = athletemodel.get_from_store()

from_data = cgi.FieldStorage()
athlete_name = from_data['which_athlete'].value

print(yate.start_response())
print(yate.include_header('Data'))
print(yate.header("Athlete:" + athlete_name + " ,Dob" + athletes[athlete_name].dob + "."))
print(yate.para("Top times:"))
print(yate.u_list(athletes[athlete_name].top3))
print(yate.include_footer({"Home":"/index.html", "selecter anthoer":"generate_list.py"}))


