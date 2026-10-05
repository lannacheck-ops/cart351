import requests

#url to the StarWars API
url = "https://swapi.info/api/planets"

#make request
response = requests.get(url) 
#get the response as json
data = response.json() 
#print
for item in data:
    print(f"Name: {item['name']} Diameter: {item['diameter']} Population: {item['population']}")
# print(data["name"])
print(type(data))
# print(data.keys())