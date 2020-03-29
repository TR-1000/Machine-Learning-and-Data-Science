import requests
from bs4 import BeautifulSoup
req = requests.get("http://localhost:8080/planets.html")
soup = BeautifulSoup(req.text, "html.parser")

planets_table = soup.select('tr.planet') # list containing the table
table_rows = soup.find_all("tr", {"class":"planet"}) # bs4 object containing the table
table = soup.find("table")
table_data = soup.find_all("td")

planet_list = []
for planet in table_rows:
    planet_data = planet.find_all("td")
    planet_list.append(
        {
            'image':planet_data[0].img.get("src"),
            'name':planet_data[1].text.strip(),
            'mass':planet_data[2].text.strip(),
            'diameter':planet_data[3].text.strip(),
            'name_origin':planet_data[4].text.strip(),
            'wiki_link':planet_data[5].a.get("href"),
        }
    )
