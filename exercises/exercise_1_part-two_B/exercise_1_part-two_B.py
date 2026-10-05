import requests

#url to the StarWars API
url = "https://swapi.info/api/planets"

#make request
response = requests.get(url) 
#get the response as json
data = response.json() 
#print
# for item in data:
#     print(f"Name: {item['name']} Diameter: {item['diameter']} Population: {item['population']}")
from rich.console import Console
from rich.table import Table

table = Table(title="STAR WARS API")

table.add_column("Name", style="cyan")
table.add_column("Diameter",  style="magenta")
table.add_column("Population",  style="green")
for item in data:
    table.add_row(item['name'], item['diameter'], item['population'])

console = Console()
console.print(table)
# print(data["name"])
print(type(data))
# print(data.keys())