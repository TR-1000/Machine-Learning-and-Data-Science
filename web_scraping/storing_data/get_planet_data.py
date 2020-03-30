import requests
import csv
from bs4 import BeautifulSoup
# python -m http.server 8080

def get_planet_data():
    req = requests.get("http://localhost:8080/planets.html")
    soup = BeautifulSoup(req.text,"html.parser")

    planet_rows =  soup.html.body.div.table.findAll("tr", {"class": "planet"})
    def to_dict(tr):
        tds = tr.findAll("td")
        planet_data = dict()
        planet_data['Name'] = tds[1].text.strip()
        planet_data['Mass'] = tds[2].text.strip()
        planet_data['Radius'] = tds[3].text.strip()
        planet_data['Description'] = tds[4].text.strip().replace("\r\n                    "," ")
        planet_data['MoreInfo'] = tds[5].findAll("a")[0]["href"].strip()
        return planet_data
    planets = [to_dict(tr) for tr in planet_rows]
    return planets
if __name__ == "__main__":
    print(get_planet_data())


planets = get_planet_data()

with open('../www/planets.csv','w+',newline='') as csvFile:
    writer = csv.writer(csvFile)
    writer.writerow(['Name', 'Mass', 'Radius', 'Description', 'MoreInfo'])
    for planet in planets:
        writer.writerow([planet['Name'], planet['Mass'],planet['Radius'], planet['Description'], planet['MoreInfo']])
