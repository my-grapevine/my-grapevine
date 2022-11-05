import json
from pprint import pprint
import requests as req
from datetime import date, timedelta

location = ((str("london")).lower()).replace(" ", "+")
query = ((str("ancient")).lower()).replace(" ", "+")
today = date.today().strftime("%Y-%m-%d")
next_month = (date.today() + timedelta(days=30)).strftime("%Y-%m-%d")
link = f"https://gears.artfund.org/search?contentTypes[]=museums&contentTypes[]=exhibitions&contentTypes[]=events&sort=&filter=contentChannels%3Dhas%3Dweb%3BstartDate%3Dlte%3D{today}%3BendDate%3Dgte%3D{next_month}%3B&limit=20&offset=0"
search_url = f"https://gears.artfund.org/search?contentTypes[]=museums&contentTypes[]=exhibitions&contentTypes[]=events&contentTypes[]=guides&search={location}+{query}&sort=&filter=contentChannels%3Dhas%3Dweb%3BstartDate%3Dlte%3D{today}%3BendDate%3Dgte%3D{next_month}%3B&limit=30&offset=0"

response = req.get(link)
event_data = response.json()

search_response = req.get(search_url)
search_event_data = search_response.json()
# print(event_data)
# clean_event_data = json.dumps(search_event_data, indent=4)
# print(clean_event_data)

for event in search_event_data['data']:
        id = event['id']
        name = event['attributes']['title']
        image_url = event['attributes'].get('image')
        if image_url is None:
                continue
        elif "srcset" in event['attributes']['image']:
                image_url = event['attributes']['image']['srcset']['md']
        else:
                image_url = event['attributes']['image']['src']
        city = event['attributes']['museum']['town']
        dates = event['attributes']['dateRange']
        venue = event['attributes']['museum']['title']
        classification = (str(event['attributes']['search']['eventType'])).replace("['", "").replace("']", "").replace("[]", "n/a")
        start_date = event['attributes']['startDate']
        url_date = f'{start_date.replace("-", "/")}/'
        slug = event['attributes']['slug']
        url = f'https://www.artfund.org/explore/exhibitions/{url_date}{slug}'
        if url != "https://www.artfund.org/explore/exhibitions?expired":
                print(f"- {id} , {name}, {image_url}, {city}, {dates}, {venue}, {classification}, {url}")

