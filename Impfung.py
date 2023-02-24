from requests import Session
import simplepush
import json

with Session() as s:
	pfizer = s.get('https://www.doctolib.de/availabilities.json?start_date=2020-05-09&visit_motive_ids=2769409&agenda_ids=456184').json()
	astra = s.get('https://www.doctolib.de/availabilities.json?start_date=2020-05-09&visit_motive_ids=2773120&agenda_ids=456184').json()

	if pfizer["availabilities"]:
		simplepush.send("myKey", "Impfstoff", "Neuer Biontech Impftermin")
		print("Neu Biontech!")

	if astra["availabilities"]:
		simplepush.send("myKey", "Impfstoff", "Neuer AstraZeneca Impftermin")
		print("Neu AstraZeneca!")
