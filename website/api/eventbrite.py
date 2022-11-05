from datetime import datetime, timedelta
import requests
import requests as req
import json
from bs4 import BeautifulSoup

url = 'https://www.eventbrite.com/d/united-kingdom--london/events--this-month/?page=1'
page = req.get(url)

html = BeautifulSoup(page.content, 'html.parser')
event_data = json.loads(str(html.select("[type='application/ld+json']")[0].contents[0]))
search_event_data = json.dumps(json.loads(str(html.select("[type='application/ld+json']")[0].contents[0])), indent=4)
all_event_data = json.loads(str(html.select("[type='application/ld+json']")[0].contents[0]))

# print(type(search_event_data))
# print(search_event_data)
# print(type(all_event_data))
# print(all_event_data)
# print(event_data)
# print(all_event_data[0]['image'])
# print(all_event_data[0]['location']['geo']['latitude'])
# for info in all_event_data:
#     longitude = all_event_data[0]['location']['geo']['longitude']
#     print(longitude)

# for index in len(all_event_data):
#     for key in all_event_data[index]:
#         # latitude = all_event_data[0]['location']['geo']['latitude']
#         # dict = all_event_data[index]
#         print(all_event_data[index])
#


# for index in range(len(all_event_data)):
#     for key in all_event_data[index]:
#         print(all_event_data[index][key])




# for event in all_event_data:
#     for index in range(len(all_event_data)):
#         if 'latitude' in all_event_data:
#             latitude = all_event_data[0]['location']['geo']['latitude']
#         else:
#             latitude = ""
        # longitude = event[0]['location']['geo']['longitude']
        # id = (f'{latitude}{longitude}').replace(".", "").replace("-", "")
        # name = event[0]['name']
        # image_url = event[0]['image'].get('image')
        # city = event[0]['location']['address']['addressLocality']
        # start_date = event[0]['startDate']
        # end_date = event[0]['endDate']['dateRange']
        # dates = f'{start - date} - {end_date}'
        # venue = event[0]['location']['name']
        # classification = event[0]['description']
        # url = event[0]['url']
        # print(f"- {latitude}")
        # print(f"- {id} , {name}, {image_url}, {city}, {dates}, {venue}, {classification}, {url}")
#
# def search(query):
#     event_data = []
#     try:
#         response = req.get(
#             f"https://www.eventbrite.com/d/united-kingdom--london/events--this-month/?page=1")
#         events = response.json()['_embedded']['events']
#     except (KeyError, requests.exceptions.RequestException):
#         events = []
#
#     for event in events:
#         new_event = {
#             latitude = event[0]['location']['geo']['latitude'],
#             longitude = event[0]['location']['geo']['longitude'],
#             id = (f'{latitude}{longitude}').replace(".", "").replace("-", ""),
#             name = event[0]['name'],
#             image_url = event[0]['image'].get('image'),
#             city = event[0]['location']['address']['addressLocality'],
#             start_date = event[0]['startDate'],
#             end_date = event[0]['endDate']['dateRange'],
#             dates = f'{start - date} - {end_date}',
#             venue = event[0]['location']['name'],
#             classification = event[0]['description'],
#             url = event[0]['url']
#         }
#         event_data.append(new_event)
#     return

#
def get_events():
    next_month = (datetime.today() + timedelta(days=30)).strftime("%Y-%m-%dT%H:%M:%SZ")

    data = []
    for page_number in range(1, 3):
        try:
            response = req.get(f"https://www.eventbrite.com/d/united-kingdom--london/events--this-month/?page={page_number}")
            html = BeautifulSoup(response.content, 'html.parser')
            search_event_data = json.dumps(json.loads(str(html.select("[type='application/ld+json']")[0].contents[0])),
                                       indent=4)
            data.extend(page.json())
        except (KeyError, requests.exceptions.RequestException, TypeError):
            break

    image_urls = set()
    events = []
    for event in data:
        is_duplicate = any(event['image'] in image_urls for image in event)
        if not is_duplicate:
            events.append({
                'name': event['name'],
                'image_url': event['image'],
                'city': event['location']['address']['addressLocality'],
                'start_date' : event['startDate'],
                'end_date' : event['endDate']['dateRange'],
                'dates' : f'{start_date} - {end_date}',
                'venue' : event['location']['name'],
                'classification' : event['description'],
                'url' : event['url']
            })
            [image_urls.add(event['image']) for image in event]
        print(events[:24])
        return events[:24]


