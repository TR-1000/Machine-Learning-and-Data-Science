import requests
from bs4 import BeautifulSoup


url = "https://www.python.org/events/pythonevents"
req = requests.get(url)
soup = BeautifulSoup(req.text, "html.parser")

# -This was my way-
# events = soup.select("ul.list-recent-events.menu")
# events_list = events[0].select("li")

#-This way is cleaner-
events = soup.find('ul', {'class': 'list-recent-events'}).find_all('li')

# for event in events:
#     event_details = {}
#     event_details['name'] = event.find('h3').find("a").text
#     event_details['location'] = event.find('span', {'class', 'event-location'}).text
#     event_details['time'] = event.find('time').text
#     #Then append each event_details dict to a list

events_list =[]
for event in events:
    events_list.append({
        'name':event.h3.text,
        'location':event.select('span.event-location')[0].text,
        'date':event.time.text
    })

print(events_list)
