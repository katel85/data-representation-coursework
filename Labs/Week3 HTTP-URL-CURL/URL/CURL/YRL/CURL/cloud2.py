import requests
import json

url = "https://opendata.housing.gov.ie/dataset/a9d1a550-fbdb-46ce-84ee-24ae9199c406/resource/5cedd7c8-5002-4b82-9665-866d662b16b4/download/general_election_2020_count_details.json"
response = requests.get(url)
data = response.json()
with open("election.json", "w") as fp:
   json.dump(data, fp)

candidates = data["Candidate surname"]
print(candidates)
#rate = euroobject["rate"]
#print(rate)