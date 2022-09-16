import json
import requests


# aStudenten = '[{"Voornaam":"Floris", "achternaam":"Ruysdaal"}, {"Voornaam":"Julia", "achternaam":"Gomez"},{"Voornaam":"Anusha", "achternaam":"Verberge"}]'

# data_Studenten = json.loads(aStudenten)

# print(data_Studenten)

# for student in data_Studenten:
#     print(student["achternaam"])


# strStudenten = "".join(aStudenten)
# i = strStudenten.find("Floris")
# print (i)





stalling = requests.get("https://stallingsnet.nl/api/1/parkingcount/utrecht")

infoStalling = json.loads(stalling.text)


for Straatnaam in infoStalling:
    if Straatnaam["freePlaces"] == 0:
        print(Straatnaam["facilityName"], "vol")
    else:
        print(Straatnaam["facilityName"], Straatnaam["freePlaces"])
