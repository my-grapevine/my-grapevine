import json

import requests as req
from datetime import date, timedelta

today = date.today().strftime("%Y-%m-%d")
next_month = (date.today() + timedelta(days=30)).strftime("%Y-%m-%d")
url = f"https://gears.artfund.org/search?contentTypes[]=museums&contentTypes[]=exhibitions&contentTypes[]=events&sort=&filter=contentChannels%3Dhas%3Dweb%3BstartDate%3Dlte%3D{today}%3BendDate%3Dgte%3D{next_month}%3B&limit=20&offset=0"

response = req.get(url)
event_data = response.json()


# print(event_data)

# start_url = f'https://www.artfund.org/explore/exhibitions/2022/10/21/{link_url}'
# print(link)

clean_event_data = json.dumps(event_data, indent=4)
print(clean_event_data)
# url_slug = response.json['data']
# print(url_slug)

#
# def get_event_link(event_data):
#     try:
#         response = req.get(
#             f"https://gears.artfund.org/search?contentTypes[]=museums&contentTypes[]=exhibitions&contentTypes[]=events&sort=&filter=contentChannels%3Dhas%3Dweb%3BstartDate%3Dlte%3D{today}%3BendDate%3Dgte%3D{next_month}%3B&limit=20&offset=0")
#         event = response.json()
#         for event in event_data:
#             link = event['attributes']['museum']['slug']
#             print(link)
#         return {
#             'link': event['attributes']['museum']['slug'],
#         }
#     except (KeyError, req.exceptions.RequestException):
#         return
# #
# #
# print(get_event_link(event_data))

